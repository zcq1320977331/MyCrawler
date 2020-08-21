import requests,random
from lxml.html import etree
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import pymongo

#连接数据库
client = pymongo.MongoClient('localhost',27017)

#选择pub_urls数据库中的urls集合,取出出版社对应的url
read_db = client.pub_urls.urls

#选择book数据库中的urls集合进行保存
save_db = client.book.urls

#设置线程池
pool = ThreadPoolExecutor(4)

#构造请求头
headers = {
    'User-Agent':UserAgent().chrome
}


#定义一个类,实现获取出版社最新发行的图书信息url功能
class GetBookUrls(object):
    '''
    start_num:获取开始前的数据量
    pub_urls_dict:存放各出版社主页面的名称和对应url
    pool:数据请求量较大,选择性的使用代理
    start_get():从pub_urls_dict获取url,进行解析存储
    save_mongodb():存放到mongodb数据库
    get_all_data():利用多线程优势进行存储
    '''
    def __init__(self,ip_pool=None):
        self.start_num = save_db.count()
        self.pub_urls = list(read_db.find())
        self.pool = ip_pool

    def start_get(self):

        # 直到解析完所有,否则一直循环
        while self.pub_urls:
            #获取到一个需要解析url
            url = self.pub_urls.pop()['url']
            #判断是否使用代理进行请求
            if self.pool == None:
                response = requests.get(url,headers = headers,)
            else:
                response = requests.get(url,headers = headers,proxies=random.choice(self.pool))

            #使用xpath进行解析
            e = etree.HTML(response.text)
            #获取相关的信息
            names = e.xpath('//div[@class="col-xs-12 col-md-6 new_chu"]/a/text()')
            urls = e.xpath('//div[@class="col-xs-12 col-md-6 new_chu"]/a/@href')
            #将信息存入数据库
            for name, url in zip(names, urls):
                dic_data = {
                    'name': name,
                    'url': url
                }
                self.save_mongodb(dic_data)

    def save_mongodb(self,dic_data):
        #将传递过来的数据存入数据库中
        for name,url in dic_data.items():
            #去重后存入
            if save_db.count({'url': url}) == 0:
                print({'name':name,'url':url})
                save_db.insert({'name':name,'url':url})


    def get_all_data(self):
        # 根据电脑核数开启线程
        f1 = pool.submit(self.start_get)
        f2 = pool.submit(self.start_get)
        f3 = pool.submit(self.start_get)
        f4 = pool.submit(self.start_get)
        while True:
            # 当所有线程结束时关闭线程池,返回更新的数据数量
            if f1.done() and f2.done() and f3.done() and f4.done():
                pool.shutdown()

                # 获取结束时的数据量
                end_num = save_db.count()
                return end_num - self.start_num

if __name__ == '__main__':
    '''
    测试
    '''
    get_book_urs = GetBookUrls()
    data = get_book_urs.get_all_data()
    print(data)

