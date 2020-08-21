import pymongo
class GetGoodsInfoPipeline:
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