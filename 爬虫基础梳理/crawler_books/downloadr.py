#http://www.cnpub.com.cn/index.php?m=content&c=index&a=lists&catid=19&cbdi=%E6%9D%AD%E5%B7%9E&she=%E4%B8%AD%E5%9B%BD%E4%B9%A6%E7%B1%8D%E5%87%BA%E7%89%88%E7%A4%BE&times=&title=%E8%BF%90%E7%AD%B9%E5%AD%A6
import requests
from lxml.html import etree
data={
    'cbdi':'杭州',
    'she':'中国书籍出版社',
    'title':'运筹学',
}
url ='http://www.cnpub.com.cn/index.php?'
requests.post(url,data=data,)