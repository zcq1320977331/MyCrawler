# from scrapy.cmdline import execute
# execute('scrapy crawl shoe_products'.split())
# execute('scrapy crawl new_product'.split())
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 根据项目配置获取 CrawlerProcess 实例
process = CrawlerProcess(get_project_settings())

# 添加需要执行的爬虫
spider_list=[
    'new_product',
    'shoe_products',
    'accessory_products',
    'athletic_wear_products',
    'nursing_products',
    'outlet_products',
    'sale_products',

    'get_new_product',
    'get_shoe_products',
    'get_accessory_products',
    'get_athletic_wear_products',
    'get_nursing_products',
    'get_outlet_products',
    'get_sale_products',

            ]
for spider in spider_list:
    process.crawl(spider)


# 执行
process.start()