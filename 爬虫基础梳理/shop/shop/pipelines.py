# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ShopPipeline:
    def open_spider(self,spider):
        self.filename = open('movie.txt','w',encoding='utf8')
    def process_item(self, item, spider):
        self.filename.write(str(item)+'\n')
        print(item)
        return item
    def close_spider(self,spider):
        self.filename.close()

class DoupoPipeline:
    def open_spider(self,spider):
        self.filename = open('doupo.txt','w',encoding='utf8')
    def process_item(self, item, spider):
        self.filename.write(str(item['zhangjie'])+'\n\n'+''.join(item['neirong']).strip().replace('\r','').replace('\n\n','\n')+'\n\n'+str(item['next_url'])+'\n\n')
        return item
    def close_spider(self,spider):
        self.filename.close()

class DouluoPipeline:
    def open_spider(self,spider):
        self.filename = open('douluo.txt','w',encoding='utf8')
    def process_item(self, item, spider):
        self.filename.write(str(item['zhangjie'])+'\n\n'+''.join(item['neirong']).strip().replace('\r','').replace('\n\n','\n')+'\n\n'+str(item['next_url'])+'\n\n')
        return item
    def close_spider(self,spider):
        self.filename.close()