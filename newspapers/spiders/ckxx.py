#coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from newspapers.items import NewspapersItem
import json

class CkxxSpider(BaseSpider):
    name = "ckxx"
    allowed_domains = ["cankaoxiaoxi.com"]
    start_urls = (
        'http://china.cankaoxiaoxi.com/2011/0830/1499.shtml',
        )
    download_delay = 1

    def parse(self, response):
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
