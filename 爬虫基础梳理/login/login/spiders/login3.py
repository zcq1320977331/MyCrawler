# -*- coding: utf-8 -*-
import scrapy
import re
class Login1Spider(scrapy.Spider):
    name = 'login3'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        hxz = re.findall(r'"__hash__":"(.+)"',response.text)[0]
        print(hxz)
        yzm_url = response.xpath('//img/@data-url').extract_first()
        yield scrapy.Request(yzm_url,callback=self.parse_yzm,meta={'hxz':hxz})

    def parse_yzm(self, response):
        with open('yzm.jpg','wb') as f:
            f.write(response.body)
        code = input('请输入验证码:')
        hxz = response.request.meta['hxz']
        form_data={
            'username': 'zcq1320977331',
            'password': 'zcq13781240894',
            'setcookie': '14',
            'checkCode':code,
            'next': '/',
            'source': 'passport',
            "__hash__": hxz,
        }
        login_url='https://passport.ganji.com/login.php?next=/'
        yield scrapy.FormRequest(login_url,formdata=form_data,callback=self.paser_res)
        url = 'http://www.ganji.com/vip/?_rid=0.345213864687518'
        print('111111111111111111111111111111111111111111')
        yield scrapy.Request(url, callback=self.paser_res)
    def paser_res(self,response):
        print('111111111111111111111111111111111111111111')
        print(response.text)
        url = 'http://www.ganji.com/vip/?_rid=0.345213864687518'
        print('111111111111111111111111111111111111111111')
        yield scrapy.Request(url, callback=self.paser_res)
    def paser_res(self,response):
        print(response.text)