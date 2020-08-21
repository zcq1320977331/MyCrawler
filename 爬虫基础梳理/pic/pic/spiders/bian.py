# -*- coding: utf-8 -*-
import scrapy
# from pic.items import ImagesItem
class BianSpider(scrapy.Spider):
    name = 'bian'
    allowed_domains = ['netbian.com']
    start_urls = ['http://www.netbian.com/']

    def parse(self, response):
        #出现No module named 'PIL',需要安装pip install pillow 解决
        # item = ImagesItem()
        image_urls = response.xpath('//div[@class="list"]//img/@src').extract()
        image_names = response.xpath('//div[@class="list"]//img/@alt').extract()
        yield {
            'image_urls':image_urls,
            'image_names':image_names
        }
        #默认传入图片列表,key值为image_urls
        # item["image_urls"]=[image_url]
        # print(item)
        # return item
