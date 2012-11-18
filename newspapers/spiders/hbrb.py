from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newspapers.items import NewspapersItem

class HbrbSpider(CrawlSpider):
    name = 'hbrb'
    allowed_domains = ['hbrb.cnhubei.com']
    start_urls = ['http://hbrb.cnhubei.com/html/hbrb/20100101/hbrb1.html']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'html\/hbrb\/[0-9]{8}\/hbrb[0-9]{1,}\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = NewspapersItem()
        i['title'] = hxs.select('//table[@id=\'Table17\']/tr[2]/td/text()').extract()
        i['text'] = hxs.select('//div[@id=\'copytext\']/font/text()').extract()
        i['category'] = hxs.select('//table[@id=\'Table16\']/tr[1]/td[3]/text()').extract()
        i['date'] = hxs.select('//table[@id=\'Table16\']/tr[1]/td[5]/text()').extract()
        return i
