from fake_useragent import UserAgent
import random
# IP_POOL = ['http://58.218.214.165:9491','http://58.218.200.229:3653','http://113.76.130.80:4272']
IP_POOL=[]#动态设置代理,或者自行连接IP数据库
class UserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent',UserAgent().random)
        # request.meta['proxy'] = 'http://ip+port'
        # request.meta['proxy'] = 'http://user:password@ip+port'
        if IP_POOL:
            request.meta['proxy'] = random.choice(IP_POOL)

#58.218.214.165:9491
#171.90.63.136

#58.218.200.229:3653
#106.115.35.178

#113.76.130.80:4272
#113.76.130.80