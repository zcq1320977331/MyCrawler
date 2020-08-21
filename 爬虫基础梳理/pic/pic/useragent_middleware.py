from fake_useragent import UserAgent
useragent=UserAgent()#实例化对象
print(useragent.random)#随机生成
class MyUserAgent(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', useragent.random)
        #或者request.headers.setdefault(b'User-Agent', UserAgent().random)
