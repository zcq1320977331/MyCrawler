# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy import signals
import pymongo
from time import sleep
client = pymongo.MongoClient('localhost', 27017)
read_db = client.accessory_products.goods_urls
save_db = client.accessory_products_goods.goods_info

class UaSpider(scrapy.Spider):
    def __init__(self):
        self.num = 1
    name = 'text'
    allowed_domains = ['ua.comm']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {'online_mall_crawl.selenium_middlewares.SeleniumWares': 400}, }
    # start_urls = ['http://www.httpbin.org/get','http://www.httpbin.org/get','http://www.httpbin.org/get']
    def start_requests(self):
        url_list = list(read_db.find().skip(self.num-1).limit(1))
        self.num+=1
        url = url_list[0]['url']
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(UaSpider,cls).from_crawler(crawler, *args, **kwargs)
        spider.chrome = webdriver.Chrome()
        crawler.signals.connect(spider.spider_closed,signal = signals.spider_closed)
        return spider
    def spider_closed(self,spider):
        spider.chrome.quit()
        print('爬虫结束了')
    def parse(self, response):
        print(response.text)
        goods_url = list(read_db.find().skip(self.num - 1).limit(1))[0]
        goods_name = ''.join(response.xpath('//div[@class="product-hero"]/h1/text()').extract())
        goods_price = ''.join(response.xpath('//span[@data-id="current-price"]/text()').extract())
        goods_colour = ''.join(response.xpath('//div[@class="grid-row colour-section"]//text()').extract())
        goods_picture = ''.join(response.xpath('//img[@class][@alt="Thumbnail 1 of 4"]/@src').extract())
        goods_description = ''.join(response.xpath('//div[@class="product-description"]//text()').extract())
        goods_details = ''.join(response.xpath('//div[@class="brand-description"]//text()').extract())
        data={
            'goods_url':goods_url,
            'goods_name': goods_name,
            'goods_price': goods_price,
            'goods_colour': goods_colour,
            'goods_picture': goods_picture,
            'goods_description': goods_description,
            'goods_details': goods_details,
        }
        save_db.insert(data)
        sleep(1)
        url_list = list(read_db.find().skip(self.num - 1).limit(1))
        self.num += 1
        url = url_list[0]['url']
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
