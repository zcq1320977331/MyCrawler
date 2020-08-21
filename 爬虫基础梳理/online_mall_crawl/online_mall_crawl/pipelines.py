# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class NewProductPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.new_product.goods_urls
    def process_item(self, item, spider):
        # item1=dict(item1)
        if self.db.count({'url':item['url']})==0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()

class ShoeProductsPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.shoe_products.goods_urls
    def process_item(self, item, spider):
        # item2 = dict(item2)
        if self.db.count({'url':item['url']})==0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()

class AccesssoryProductsPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.accessory_products.goods_urls
    def process_item(self, item, spider):
        # item2 = dict(item2)
        if self.db.count({'url':item['url']}) == 0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()

class AthleticWearProductsPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.athletic_wear_products.goods_urls
    def process_item(self, item, spider):
        # item2 = dict(item2)
        if self.db.count({'url':item['url']}) == 0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()

class NursingProductsPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.nursing_products.goods_urls
    def process_item(self, item, spider):
        # item2 = dict(item2)
        if self.db.count({'url':item['url']}) == 0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()

class OutletProductsPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.outlet_products.goods_urls
    def process_item(self, item, spider):
        # item2 = dict(item2)
        if self.db.count({'url':item['url']}) == 0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()

class SaleProductsPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.sale_products.goods_urls
    def process_item(self, item, spider):
        # item2 = dict(item2)
        if self.db.count({'url':item['url']}) == 0:
            self.db.insert(item)
        return item
    def close_spider(self, spider):
        self.client.close()