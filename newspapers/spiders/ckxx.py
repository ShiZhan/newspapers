#!/usr/bin/python
#coding=utf-8
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from newspapers.items import NewspapersItem

class CkxxSpider(CrawlSpider):
    name = 'ckxx'
    download_delay = 1.5

    allowed_domains = ['cankaoxiaoxi.com', 'localhost']
    start_urls = ['http://mil.cankaoxiaoxi.com/2012/1129/127185.shtml']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/[0-9]{4}/[0-9]{4}/[0-9]+.shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = NewspapersItem()
        i['title'] = hxs.select('//h2[@class="h2 b fz-24 mar-b-20"]/text()').extract()
        # some page has author following date
        i['date']  = hxs.select('//span[@class="cor666"]/text()[1]').extract
        # just use subtitle for abstract
        i['subtitle'] = hxs.select('//div[@class="bd-blue bg-white pad-10 mar-b-20 cont-detail"]/p/text()').extract()
        # contains "报道" & "延伸阅读"
        i['text']     = hxs.select('//div[@class="fs-small cont-detail det" and @id="ctrlfscont"]').extract()
        i['category'] = hxs.select('//span[@class="cor-blue"]/text()').extract()
        i['editor']   = hxs.select('//span[@class="f-r cor666"]/text()').extract()

        return i
