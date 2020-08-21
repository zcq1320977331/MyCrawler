from gevent import monkey
monkey.patch_all()
import requests,gevent
from lxml.html import etree
import random
import time
start = time.time()
def get():
    try:
        url ='http://www.httpbin.org/get'#返回请求头信息
        response = requests.get(url)
        print(response.text)
        print('\n--------------------------------------------------------\n')
    except:
        print('失败')
lst = []
for i in range(10):
    lst.append(gevent.spawn(get))

gevent.joinall(lst)
end = time.time()
print(end-start)