import requests
from fake_useragent import UserAgent
url = 'https://www.baidu.com/s'
headers = {
    'User-Agent':UserAgent().chrome
}
params = {
    'wd':'python'
}
response = requests.get(url,headers = headers,params = params)
print(response.text)