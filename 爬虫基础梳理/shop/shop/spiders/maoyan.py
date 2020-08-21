# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        print(response.text)
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/a/text()').extract()
        print(names)
        score_list = response.xpath('//div[@class="channel-detail channel-detail-orange"]')


