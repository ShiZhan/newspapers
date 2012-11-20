from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newspapers.items import NewspapersItem

class HbrbSpider(CrawlSpider):
    name = 'hbrb'
    download_delay = 1.5

    allowed_domains = ['hbrb.cnhubei.com', 'localhost']
    start_urls = ['http://localhost/2012test.html']

    rules = (
        # daily index
        Rule(SgmlLinkExtractor(
            restrict_xpaths='/html/body/a',
            allow=r'html\/hbrb\/[0-9]{8}\/index.html'),
            follow=True),
        # page index
        Rule(SgmlLinkExtractor(
            allow=r'html\/hbrb\/[0-9]{8}\/hbrb[0-9]{1}.html'),
            follow=True),
        # report
        Rule(SgmlLinkExtractor(
            allow=r'html\/hbrb\/[0-9]{8}\/hbrb[0-9]{3,}\.html'),
            callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = NewspapersItem()

        i['subtitle'] = hxs.select('//table[@id=\'Table17\']/tr[1]/td/text()').extract()
        i['title']    = hxs.select('//table[@id=\'Table17\']/tr[2]/td/text()').extract()
        i['text']     = hxs.select('//div[@id=\'copytext\']/font/text()').extract()
        i['category'] = hxs.select('//table[@id=\'Table16\']/tr[1]/td[3]/text()').extract()
        date_raw      = hxs.select('//table[@id=\'Table16\']/tr[1]/td[5]/text()').extract()
        i['date']     = ' '.join(date_raw).split()

        return i
