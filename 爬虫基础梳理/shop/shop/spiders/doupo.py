# -*- coding: utf-8 -*-
import scrapy

class DoupoSpider(scrapy.Spider):
    name = 'doupo'
    allowed_domains = ['tycqxs.com',]
    start_urls = ['http://www.tycqxs.com/57_57672/21597158.html']
    custom_settings = {'ITEM_PIPELINES':{'shop.pipelines.DoupoPipeline': 300}}
    #设置管道
    def parse(self, response):
        zhangjie = response.xpath('//h1/text()').extract_first()
        neirong = response.xpath('//div[@id="content"]/text()').extract()
        next_url = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract_first()
        yield {
            'zhangjie':zhangjie,
            'neirong':neirong,
            'next_url':response.urljoin(next_url)
        }
        new_url = response.urljoin(next_url)
        print(new_url)
        yield scrapy.Request(url=new_url, callback=self.parse,dont_filter=True)

