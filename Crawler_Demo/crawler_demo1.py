import time
import requests
from bs4 import BeautifulSoup
import re
start = time.clock()


class Baby(object):
    
    def __init__(self):
        self.name = 'Baby'
        self.age = '3'
        self.ability_1 = 'Crawl'
        self.ability_2 = 'Grab'
        self.function = Function()
        
    
        

    def Crawl1(self,number):
        i=0
        self.function.urls.add('https://www.baidu.com/')
        while i<= number:
            try:
                url = self.function.urls.pop()
                self.function.old_urls.add(url)
                print('crawl%d:'%i,url)
                #print('old_urls:',self.function.old_urls)
                #print('urls',self.function.urls)
                html = self.function.GetHtml(url)
                new_url = self.function.Geturl(html)
                self.function.urls.add(new_url)
                i+=1
            except:
                print('2')
            

    def Grab(self):
        pass


class Function(object):
    
    def __init__(self):
        self.name = 'Function'
        self.function_1 = 'SaveUrl'
        self.function_2 = 'GetUrl'
        self.function_3 = 'GetHtml'
        self.urls = set()
        self.old_urls = set()
        
    def SaveUrl(self,url):
        pass




        
    def Geturl(self,html):
        try:
            soup = BeautifulSoup(html,'html.parser')
            for link in soup.find_all('a'):
                url=link.get('href')
                if 'http'in url and 'com'in url and url not in self.old_urls:
                    self.urls.add(url)
                    print (url)
        except:
            print('1')
                   


              

    
    def GetHtml(self,url):
        try:
            address = {'user-agent':'Mozilla/5.0'}
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            r.raise_for_status()
            html = r.text
            return html
        except:
            print('Request error')

        



baby = Baby()

baby.Crawl1(100)















end = time.clock()
print('Running time:%s' %(end-start))
