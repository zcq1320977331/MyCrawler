# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DouluoSpider(CrawlSpider):
    name = 'douluo'
    allowed_domains = ['tycqxs.com']
    start_urls = ['http://www.tycqxs.com/54_54196/']
    custom_settings = {'ITEM_PIPELINES': {'shop.pipelines.DoupoPipeline': 300}}
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]//dd[10]/a'),callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        zhangjie = response.xpath('//h1/text()').extract_first()
        neirong = response.xpath('//div[@id="content"]/text()').extract()
        next_url = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract_first()
        print(zhangjie)
        yield {
            'zhangjie': zhangjie,
            'neirong': neirong,
            'next_url': response.urljoin(next_url)
        }

