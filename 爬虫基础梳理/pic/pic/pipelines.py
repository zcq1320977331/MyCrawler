# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
#重写方法,改文件名称
class PicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_name,image_url in zip(item['image_names'],item['image_urls']):
            print(image_url,image_name)
            yield scrapy.Request(image_url,meta={'image_name':image_name})

    def file_path(self, request, response=None, info=None):
        print(type(request.meta['image_name']))
        return request.meta['image_name']+'.jpg'

