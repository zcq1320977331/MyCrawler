import requests
from bs4 import BeautifulSoup
import re
import os
import urllib3
url='https://i.mmzztt.com/thumb/2020/01/219871_236.jpg'
address = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=address)
r.raise_for_status()
r.encoding = r.apparent_encoding
html=r.text
soup = BeautifulSoup(html,'html.parser')
path = 'C:/Users/Administrator/Desktop/P/2.jpg'
urllib3.response.urlretrieve(path,url)
print('保存成功')