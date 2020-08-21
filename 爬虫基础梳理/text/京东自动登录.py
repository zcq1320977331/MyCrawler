from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains #动作链
import random

def get_track(distance):
    distance += 6
    track = []
    current = 0
    if distance > 100:
        mid1 = distance * 1 / 3
        mid2 = distance * 7 / 8
    else:
        mid1 = distance * 1 / 2
        mid2 = distance * 5 / 6
    t = 0.3
    v = 3
    while current < distance:
        if current < mid1:
            a = random.uniform(3, 5)
        elif current < mid2:
            a = random.uniform(0, 1)
        else:
            a = - random.uniform(9, 12)
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track

chrome = webdriver.Chrome()#创建谷歌浏览器实例
chrome.get('https://passport.jd.com/new/login.aspx?')#发送请求,打开淘宝登录地址
sleep(2)#等待加载,网络不好的话页面信息加载不出来,可以根据网速自行设定


login_account = chrome.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a')
login_account.click()

username_input = chrome.find_element_by_id("loginname")#获取用户名输入窗口
password_input = chrome.find_element_by_id("nloginpwd")#获取密码输入窗口

username_input.send_keys('13781240894')#输入用户名
password_input.send_keys('zcq13781240894')#输入密码
sleep(1)#等待加载,这里会加载滑块
#注意: 一定要先执行输入用户名和密码,才能进行下一步操作

login_button = chrome.find_element_by_id("loginsubmit")#获取登录按钮
login_button.click()#点击登录
sleep(1)

slider = chrome.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')#获取滑块
url_now = chrome.current_url
i = 0
while True:
    i=i+1
    action = ActionChains(chrome)#创建动作链
    action.click_and_hold(slider)#模拟按住滑块不松开
    try:
        track = get_track(60)
        for x in track:
            action.move_by_offset(x,0).perform()#拖动滑块到底,通过浏览器可以获取拖动的距离
            sleep(float('{:.2f}'.format(random.random())))
            action.move_by_offset(random.randint(1, 3), 0)
            sleep(float('{:.2f}'.format(random.random())))
            action.move_by_offset(float('{:.2f}'.format(random.random())), 0)
            action.move_by_offset(-float('{:.2f}'.format(random.random())), 0)
            action.release().perform()
    except:
        pass

    sleep(1)
    url = chrome.current_url
    if url != url_now:
        break
    # action.release()#释放动作链

print('登录成功',i)
# chrome.close()


