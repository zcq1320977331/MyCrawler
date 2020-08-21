class MyProxyMiddleWare:
    def process_request(self, request, spider):
        # request.meta['proxy']='http://(ip):(port)',没有用户名写法
        # request.meta['proxy']='http://username:password@(ip):(port)',有用户名写法
        request.meta['proxy'] = 'http://58.218.201.114:6905'