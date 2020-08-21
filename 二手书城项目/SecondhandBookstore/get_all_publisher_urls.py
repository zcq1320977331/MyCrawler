import requests
from lxml.html import etree
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
import pymongo

#连接mongdb数据库
client = pymongo.MongoClient('localhost',27017)

#选择pub_urls数据库中的urls集合
db = client.pub_urls.urls

#构造线程池

pool = ThreadPoolExecutor(4)

#构造请求头
headers = {
    'User-Agent':UserAgent().chrome
}

#获取全部带出版社信息的页面
url_list = ['http://www.cnpub.com.cn/index.php?m=content&c=index&a=lists&catid=12&diqu=&title=&page=' + str(x) for x in range(1, 44)]


#定义一个类,从出版社信息的页面获取所有的出版社信息的url
class GetPubUrl(object):
    '''
    start_num:获取开始前的数据量
    self.data:以字典形式存放出版社名称和对应的url
    start_get():从url_list获取url进行解析数据
    save_mongodb():将所有提取到的信息加入到数据库中
    get_all_data():类的主方法,利用多线程快速抓取页面进行解析
    '''
    def __init__(self):
        self.start_num = db.count()
        self.data = {}

    def start_get(self,):
        # 直到解析完所有,否则一直循环
        while url_list:
            # 从列表中取出一个url
            url = url_list.pop()

            # 请求获取响应
            response = requests.get(url,headers = headers)

            # 利用xpath进行解析
            e = etree.HTML(response.text)

            #获取到出版社名称和对应的url
            names = e.xpath('//div[@class="padd_20 list_chuban"]/a[1]//h4/text()')
            urls = e.xpath('//div[@class="padd_20 list_chuban"]/a/@href')

            # 获得的数据添加到self.data中
            for name, url in zip(names, urls):
                name = name.split('.')[1]
                self.data[name] = url

    def save_mongodb(self):
        # 从self.data取出信息
        for name,url in self.data.items():

            # 去重,写入数据库
            if db.count({'url':url}) == 0:
                db.insert({'name':name,'url':url})

    def get_all_data(self):

        #根据电脑核数开启线程
        f1 = pool.submit(self.start_get)
        f2 = pool.submit(self.start_get)
        f3 = pool.submit(self.start_get)
        f4 = pool.submit(self.start_get)

        while True:
            #当所有线程结束时关闭线程池,返回更新的数据数量
            if f1.done() and f2.done() and f3.done() and f4.done():
                pool.shutdown()

                # 获取结束时的数据量
                end_num = db.count()
                return end_num-self.start_num


if __name__ == '__main__':
    '''
    测试
    '''
    get_pub_urs = GetPubUrl()
    data = get_pub_urs.get_all_data()
    get_pub_urs.save_mongodb()

