import requests
import re
import threading
import os
import time

class MyBaby(object):
    def __init__(self,address):#address为了简洁只支持盘符
        self.address=address
        self.url1_list=[]#存放主页面url连接
        self.url2_list=[]#存放组图资源url连接

    def Geturl_1(self,):
        '''
        获取到所有的页面链接，
        无返回值，结果直接存在self.url1_list
        '''
        start_time = time.clock()
        print('页面资源加载开始')
        try:
            for i in range(2, 160):
                url = 'https://004647.com/list-14-%s.html' % i
                self.url1_list.append(url)
            print('页面资源加载完毕')
            end_time = time.clock()
            print('页面资源加载耗时：%.2f' % (end_time - start_time))
        except:
            pass

    def Geturl_2(self,size):
        try:
            def func2():
                '''
                1.解析主页面连接，获得组图资源连接
                2.无返回值，结果直接存在self.url2_list
                3.这里封装成函数，是因为数据请求是，I/O操作，
                    通过多线程可以提高效率
                '''
                while self.url1_list:
                    url = self.url1_list.pop()#为了避免重复，采用pop
                    size_new = len(self.url1_list)
                    resu = '数据已加载：%.2f%%' % (((size - size_new) / size) * 100)
                    print('\r%s' % resu, end='', flush=True)#时间较久，加进度条
                    html=self.GetHtml(url)#获取源码，解析，获取相关数据
                    re_url = '<ul class="detail-list">.+?</ul></div></div>'
                    ret = re.findall(re_url, html, re.S)
                    res = re.findall("https://.+?/article.+?.html", ret[0])
                    res = set(res)
                    for ele in res:#将获取到的数据写入到url2_list中
                        self.url2_list.append(ele)

            start_time = time.clock()
            print('数据资源加载开始')

            for i in range(6):
                #根据电脑CPU核数获得最优线程数，这里采用了核数*2+2
                t2 = threading.Thread(target=func2)
                t2.start()
            t2.join()
            print('数据资源加载完毕')
            end_time = time.clock()
            print('数据资源加载耗时：%.2f' % (end_time - start_time))
            #获取下加载时间
        except:
            t2 = threading.Thread(target=func2)
            t2.start()

    def GetHtml(self, url):
        '''
        获取源码的封装
        :param url: 传入url链接
        :return: 返回该连接对应源码
        '''
        try:#处理异常
            address = {'user-agent': 'Mozilla/5.0'}#虚拟请求地址，有的网站会检查是否浏览器浏览
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            r.raise_for_status()
            html = r.text#获取到源码
            return html
        except:
            pass

    def Download(self,):
        '''
        下载逻辑代码存放
        :无返回值，直接存放对应位置
        '''
        print('下载图片中')
        try:
            def save():
                try:
                    while self.url2_list:
                        url=self.url2_list.pop()#依次取，避免重复
                        html = self.GetHtml(url)#获取源码
                        ret = re.findall('<h1>(?P<name>.+?)<span> (?P<num>.+?)</span></h1>', html, re.S)
                        res = re.findall('\d+', ret[0][1], re.S)
                        file_name=ret[0][0]#获取组图名
                        N=int(res[1])#获取组图总数量
                        save_path=self.address+'爬虫照片/'#设置储存位置，从传入的盘符
                        if os.path.isdir(save_path):
                            #判断是否有该路径，有的话继续，没有创建
                            pass
                        else:
                            os.mkdir(save_path)
                        file_path = os.path.join(save_path, file_name)
                        #拼接组图文件夹，存放组图图片
                        if os.path.isdir(file_path):
                            # 判断是否有该路径，有的话继续，没有创建
                            print('%s组图已存在'%file_path)
                            pass
                        else:
                            os.mkdir(file_path)
                        for i in range(2, N):
                            #拼接组图中每张图片链接
                            str1 = '%s%s.html' % ('-', str(i))
                            new_url = url.replace('.html', str1)
                            Picture_path=os.path.join(file_path, str(i)+'.gif')
                            #拼接文件储存位置
                            if os.path.isfile(Picture_path):
                                # 判断是否有该图片，有的话跳过，没有下载
                                print('%s图片已存在'% file_name+str(i)+'.gif')
                                continue
                            else:
                                new_html = self.GetHtml(new_url)#获取到图片链接
                                data_url = re.findall('https://img.+?gif', new_html, re.S)
                                data = requests.get(data_url[0])
                                print('正在下载%s' % file_name + str(i) + '.gif')
                                with open(Picture_path, 'wb') as f:#储存图片
                                    f.write(data.content)
                                    print('%s下载完成' % (file_name + str(i) + '.gif'))
                except:
                    t3 = threading.Thread(target=save, )
                    t3.start()
            for i in range(6):
                t3= threading.Thread(target=save,)
                t3.start()
            t3.join()
        except:
            pass
    def run(self):
        '''
        主程序
        '''
        self.Geturl_1()
        base_url1_size = len(self.url1_list)
        self.Geturl_2(base_url1_size)
        self.Download()

print('''
    请输入对应序号，任意键默认为C盘
    1. C盘
    2. D盘
    3. E盘
    4. F盘
    5. G盘
    6. H盘
    ''')
dic={'2':'D:/','3':'E:/','4':'F:/','5':'G:/','6':'H:/'}
while 1:#
    add=input('请输入储存位置：')
    if dic[add] and os.path.isdir(dic[add]):
        addr=dic[add]
        break
    else:
        print('''
        磁盘不存在或者输入有误
        1. 重新输入
        2. 默认存在C盘
        3. 任意键退出程序
        ''')
        N=input('请输入对应序号：')
        if N=='1':
            continue
        elif N=='2':
            addr='C:/'
            break
        else:
            addr=None
            break

if addr==None:
    print('感谢使用')
else:
    baby = MyBaby(addr)
    baby.run()

F:\Python 项目\reptile\reptile.py