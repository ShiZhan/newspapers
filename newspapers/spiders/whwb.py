from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newspapers.items import NewspapersItem

class WhwbSpider(CrawlSpider):
    name = 'whwb'
    download_delay = 1.5

    allowed_domains = ['cjmp.cnhan.com', 'localhost']
    start_urls = ['http://localhost:9080/whwb.html']
    # allowed_domains = ['cjmp.cnhan.com']
    # start_urls = ['http://cjmp.cnhan.com/whwb/html/2012-11/20/node_22.htm']

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths='/html/body/a', allow=r'node_[0-9]{2,3}.htm'), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths='//a[@id=\'pageLink\']', allow=r'node_[0-9]{2,3}.htm'), follow=True),
        Rule(SgmlLinkExtractor(restrict_xpaths='//a/div[@id]/..', allow=r'content_[0-9]+.htm'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = NewspapersItem()

        i['subtitle'] = hxs.select('//table[5]/tbody/tr[3]/td/table/tbody/tr/td/span[1]/text()').extract()
        i['title']    = hxs.select('//strong[@style]/text()').extract()
        i['text']     = hxs.select('//div[@id=\'ozoom\']/p/text()').extract()
        i['category'] = hxs.select('//td[@class=\'px12\'][1]/strong/text()').extract()
        date_raw      = hxs.select('//span[@class=\'default\']/strong/font/text()').extract()
        i['date']     = ' '.join(date_raw).split()

        return i
