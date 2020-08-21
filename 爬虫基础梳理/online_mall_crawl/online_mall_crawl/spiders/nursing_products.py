# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from online_mall_crawl import items
class UrlsExtractSpider(CrawlSpider,):
    name = 'nursing_products'
    allowed_domains = ['asos.com']
    custom_settings = {
    'ITEM_PIPELINES': {'online_mall_crawl.pipelines.NursingProductsPipeline': 304},
    'DOWNLOADER_MIDDLEWARES': {'online_mall_crawl.middlewares.UserAgentMiddleware': 400},}
    # start_urls = ['https://www.asos.com/women/new-in/new-in-face-body/cat/?cid=2426&nlid=ww|new+in|new+products']
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//a[@data-auto-id="loadMoreProducts"]'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield scrapy.Request('https://www.asos.com/women/face-body/cat/?cid=1314&nlid=ww|face+%2B+body|shop+by+product',dont_filter=True)
    def parse_item(self, response):
        # item1 = items.NewProductItem()
        goods_urls = response.xpath('//a[@class="_3TqU78D"]/@href').extract()
        for url in goods_urls:
            # item1['url'] = url
            # yield item1
            yield {'url':url}