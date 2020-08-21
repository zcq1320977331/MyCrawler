# -*- coding: utf-8 -*-
import scrapy


class GetuaSpider(scrapy.Spider):
    name = 'getua'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://www.httpbin.org/get']#返回请求信息

    def parse(self, response):
        print(response.text)
