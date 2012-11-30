#coding=utf-8
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newspapers.items import NewspapersItem

class CkxxSpider(CrawlSpider):
    name = 'ckxx'
    allowed_domains = ['cankaoxiaoxi.com']
    start_urls = ['http://localhost:9080/ckxx.html']

    download_delay = 1

    rules = (
        Rule(SgmlLinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        content = hxs.select('//div[contains(@class,"bg-content")]')
        i = NewspapersItem()
        i['title'] = content.select('.//h2/text()').extract()
        # some page has author following date
        source_raw = content.select('.//span[@class="cor666"]/text()').extract()
        i['date'] = source_raw[0]
        # just use subtitle for abstract
        i['subtitle'] = content.select('.//div[contains(@class,"cont-detail") and not(@id)]/p/text()').extract()
        # contains "报道" & "延伸阅读"
        i['text']     = content.select('.//div[contains(@class,"cont-detail") and @id="ctrlfscont"]').extract()
        i['category'] = content.select('.//span[@class="cor-blue"]/text()').extract()
        i['editor']   = content.select('.//span[@class="f-r cor666"]/text()').extract()

        return i
