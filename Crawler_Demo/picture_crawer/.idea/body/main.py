import requests
from bs4 import BeautifulSoup
import re
new_urls = set()
new_urls.add('https://www.mzitu.com/page/2/')
old_urls = set()
def GetUrl(url):
    try:
        address = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = address)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Failure')
def GetHtml(html):
    soup = BeautifulSoup(html,'html.parser')
    for link in soup.find_all('a'):
        new_url = link.get('href')
        if 'http' in new_url and new_url not in old_urls:
            new_urls.add(new_url)
def HeadMain():
    url = new_urls.pop()
    old_urls.add(url)
    html = GetUrl(url)
    GetHtml(html)
def main():
    HeadMain()
    HeadMain()
    HeadMain()

    print(new_urls)
    print(old_urls)
main()
reg = r'src="(https.+?.pg)"'
a=re.compile(reg)
print(a)