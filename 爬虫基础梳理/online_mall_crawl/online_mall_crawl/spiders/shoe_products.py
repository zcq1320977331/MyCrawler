# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from online_mall_crawl import items
class UrlsExtractSpider(CrawlSpider,):
    name = 'shoe_products'
    allowed_domains = ['asos.com']
    custom_settings = {
    'ITEM_PIPELINES': {'online_mall_crawl.pipelines.ShoeProductsPipeline': 301},
    'DOWNLOADER_MIDDLEWARES': {'online_mall_crawl.middlewares.UserAgentMiddleware': 400},}
    # start_urls = ['https://www.asos.com/women/new-in/new-in-face-body/cat/?cid=2426&nlid=ww|new+in|new+products']
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//a[@data-auto-id="loadMoreProducts"]'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield scrapy.Request('https://www.asos.com/women/shoes/cat/?cid=4172&nlid=ww|shoes|shop+by+product',dont_filter=True)
    def parse_item(self, response):
        # item2 =items.ShoeProductsItem()
        goods_urls = response.xpath('//a[@class="_3TqU78D"]/@href').extract()
        for url in goods_urls:
            # item2['url'] = url
            # yield item2
            yield{
                'url':url
            }