# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['asos.comfir']
    start_urls = ['https://www.asos.com/women/sale/cat/?cid=7046&page={}'.format(x) for x in range(1)]

    def parse(self, response):
        #print(response.xpath('//article/a/@href').extract())
        res_uurls = response.xpath('//article/a/@href').extract()
        for url in res_uurls:
            print(url)

