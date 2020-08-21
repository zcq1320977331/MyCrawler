# -*- coding: utf-8 -*-
import scrapy

class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['ganji.com']
    # start_urls = ['http://wapi.http.cnapi.cc/index/users/login_do']
    def start_requests(self):
        url = 'https://passport.ganji.com/login.php'
        form_data={
            'phone':'13781240894',
            'password':'zcq13781240894'
        }
        yield scrapy.FormRequest(url,formdata=form_data,callback=self.parse)
    def parse(self, response):
        print(response.text)
        # yield scrapy.Request(url,callback=self.parse1)


    def parse1(self, response):
        print(response.text)