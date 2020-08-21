from scrapy.cmdline import execute
from shop.shop.commands import start_all
# execute('scrapy crawl douluo'.split())
#execute(['scrapy','crawl','first'])
execute('scrapy start_all'.split())