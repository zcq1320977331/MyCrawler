import requests,threading,pymongo,random
from lxml.html import etree
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

#连接数据库
client = pymongo.MongoClient('localhost',27017)

#选择book数据库中的urls集合,取出出版社对应的url
read_db = client.book.urls

#选择book_info数据库中的books集合进行保存
save_db = client.book_info.books

#设置线程池
pool = ThreadPoolExecutor(4)

#构造请求头
headers = {
    'User-Agent':UserAgent().chrome
}

#设置线程锁,为了使读取到的数据更精确
lock = threading.RLock()

#定义一个类,实现书籍信息的获取
class GetBookInfo(object):
    '''
    book_urls:临时存放待爬取的url
    pool:代理池
    number:动态设置一次从数据库取出多数数据
    get_data:主执行函数,获取所有书籍数据
    '''
    def __init__(self,number = 50,ip_pool = None):
        self.book_urls = []
        self.start_num = save_db.count()
        self.number = number
        self.pool = ip_pool

    def get_data(self,):
        # 返回True说明还有有未被爬取url
        if self.read_urls():
            # 直到解析完所有,否则一直循环
            while self.book_urls:
                url = self.book_urls.pop()['url']
                print(url)
                # 获取信息并保存
                self.get_url(url)

            #解析完毕后重新执行get_data,直到self.find_urls()返回False说明全部爬取完毕
            return self.get_data()
        else:
            return False

    def get_url(self,url):
        # 判断是否使用代理进行请求

        if self.pool == None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, proxies=random.choice(self.pool))

        # 使用xpath 解析
        e = etree.HTML(response.text)

        # 获取相关的信息
        book_isbn = e.xpath('//div[@class="min_h300 bookinfo"]/p[4]/text()')[0].split('：')[1]
        book_cip = e.xpath('//div[@class="min_h300 bookinfo"]/p[3]/text()')[0].split('：')[1]
        book_name = e.xpath('//div[@class="min_h300 bookinfo"]/h3/text()')[0]
        book_author = e.xpath('//div[@class="min_h300 bookinfo"]/p[1]/text()')[0].split('：')[1]
        book_publishers = e.xpath('//div[@class="min_h300 bookinfo"]/p/a/text()')[0]
        book_pub_time = e.xpath('//div[@class="min_h300 bookinfo"]/p[6]/text()')[0].split('：')[1]
        book_price = e.xpath('//div[@class="min_h300 bookinfo"]//strong/text()')[0]
        book_synopsis = e.xpath('//div[@id="tab1"]/p/text()')[0]
        book_info = {
            '_id':book_isbn,#获取IBSN编码,由于其唯一性,故可以设置为_id
            'book_cip': book_cip,#获取书籍的cip号
            'book_name': book_name,#获取书名
            'book_author': book_author,#获取作者
            'book_publishers': book_publishers,#获取出版社
            'book_pub_time': book_pub_time,#获取出版时间
            'book_price': book_price,#获取价格
            'book_synopsis': book_synopsis,#获取简介
        }

        #保存至数据库
        self.save_mongodb(book_info)


    def save_mongodb(self,info):
        #利用save的特性去重保存
        save_db.save(info)

    def get_all_data(self):
        # 根据电脑核数开启线程
        f1 = pool.submit(self.get_data)
        f2 = pool.submit(self.get_data)
        f3 = pool.submit(self.get_data)
        f4 = pool.submit(self.get_data)

        # 当所有线程结束时关闭线程池,返回更新的数据数量
        while True:
            if f1.done() and f2.done() and f3.done() and f4.done():
                pool.shutdown()

                # 获取结束时的数据量
                end_num = save_db.count()
                return end_num - self.start_num

    def read_urls(self):
        #加锁,为了防止多线程造成数据混乱
        lock.acquire()
        #获取50条信息并且返回True,如果没有获取到返回Fals
        if list(read_db.find().skip(self.number - 50).limit(50)):
            self.book_urls = list(read_db.find().skip(self.number - 50).limit(50))
            self.number += len(self.book_urls)
            #解锁,并返回True
            lock.release()
            return True
        else:
            # 解锁,并返回False
            lock.release()
            return False

if __name__ == '__main__':
    '''
    测试
    '''
    get_book_info = GetBookInfo()
    data = get_book_info.get_all_data()
    print(get_book_info.number)
