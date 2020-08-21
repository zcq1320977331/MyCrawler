# -*- coding: utf-8 -*-
import scrapy
from shop.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        names = response.xpath('//div[@class="hd"]/a/span[1]/text()').extract()
        scores = response.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract()
        # for name,score in zip(names,scores):
        #     yield {
        #     'name':name,
        #     'score':score
        #     }

        item = DoubanItem()
        for name, score in zip(names, scores):
            item['name'] = name
            item['score'] = score
            yield item