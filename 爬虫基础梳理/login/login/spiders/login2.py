# -*- coding: utf-8 -*-
import scrapy


class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['taobo.com']
    #start_urls = ['http://taobo.com/']
    def start_requests(self):
        url = 'https://cart.taobao.com/cart.htm?spm=a1z0d.6639537.1997525049.1.1e1a7484fxa5TN&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739'

        str1 = 'thw=cn; t=43f78d68be7ffabad5fbcd604b7490bc; ubn=p; ucn=center; cna=85VTF2ijCH4CAXM9zAjOjJN8; _samesite_flag_=true; cookie2=1823fcd3d09f35cc6dd0d55853cf1973; _tb_token_=b07e755a7133; sgcookie=E8RguB0F3loqwHD%2BxfUMX; unb=2766641341; uc3=vt3=F8dBxGettN31zK%2BS4Xk%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&nk2=s2FmPdYFH28Mhw%3D%3D&id2=UU8Od9YvBgJ%2FYw%3D%3D; csg=e7c8990f; lgc=%5Cu865A%5Cu62DF%5Cu5370%5Cu8C61%5Cu6B87; cookie17=UU8Od9YvBgJ%2FYw%3D%3D; dnk=%5Cu865A%5Cu62DF%5Cu5370%5Cu8C61%5Cu6B87; skt=45373b1b29b3fc2b; existShop=MTU5MDU2NTM2NQ%3D%3D; uc4=id4=0%40U22JppMX5z5lZmKwYSA42MF8ihId&nk4=0%40sR6pPvD7w1Dyn%2FUXcgQi%2FriSa1nJ; tracknick=%5Cu865A%5Cu62DF%5Cu5370%5Cu8C61%5Cu6B87; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%AE%8719; _nk_=%5Cu865A%5Cu62DF%5Cu5370%5Cu8C61%5Cu6B87; cookie1=BxUHGEGKL3hp9rdXwTYT0Hv9xpf24aweyAZjw2AZku4%3D; mt=ci=28_1; tfstk=cZbNBgGBmPUZLlLb2FT2GcpwY4GOak7cPldvjg9eOizuLoKBUsYjHBxYaOB2eyxG.; uc1=cookie21=VT5L2FSpccLuJBreK%2BBd&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&pas=0&existShop=false&cookie14=UoTV7NMV2LeonA%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cart_m=0; isg=BAsLXnO30RyQGg1IYFOGfwaemq_1oB8iszhQUH0I58qhnCv-BXCvcqk-cpxyp3ca; l=eBQMAancQD2yXQ6zBOfanurza77OSIRYYuPzaNbMiOCP9O5B55mlWZAeErY6C3GVh63BR3ykIQI6BeYBqQAonxvOUKaOYMkmn'
        lst1 = str1.split(';')
        dic = {}
        for i in lst1:
            lst2 = i.split('=')
            key = lst2[0].strip()
            value = lst2[1].strip()
            dic[key] = value
        print(dic)
        yield scrapy.Request(url,cookies=dic ,callback=self.parse)
    def parse(self, response):
        print(response.text)
