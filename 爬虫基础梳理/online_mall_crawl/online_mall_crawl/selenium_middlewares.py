from scrapy.http import HtmlResponse
import random,time
IP_POOL = ['http://58.218.92.140:6522','http://58.218.200.249:7888','http://122.242.49.57:4256']
#需要大量ip循环,此网站检测ip
class SeleniumWares:
    def process_request(self, request, spider):
        if IP_POOL:
            request.meta['proxy'] = random.choice(IP_POOL)
        url = request.url
        spider.chrome.get(url)
        show = spider.chrome.find_element_by_xpath('//a[@class="show"]')
        show.click()
        time.sleep(0.05)
        html = spider.chrome.page_source
        return HtmlResponse(url=url, body=html, request = request, encoding='utf8')
