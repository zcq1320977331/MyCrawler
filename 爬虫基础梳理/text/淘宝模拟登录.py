from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains #动作链

chrome = webdriver.Chrome()#创建谷歌浏览器实例
chrome.get('https://login.taobao.com/member/login.jhtml?')#发送请求,打开淘宝登录地址
sleep(2)#等待加载,网络不好的话页面信息加载不出来,可以根据网速自行设定

username_input = chrome.find_element_by_id("fm-login-id")#获取用户名输入窗口
password_input = chrome.find_element_by_id("fm-login-password")#获取密码输入窗口

username_input.send_keys('13781240894')#输入用户名
password_input.send_keys('zcq13781240894')#输入密码
sleep(1)#等待加载,这里会加载滑块
#注意: 一定要先执行输入用户名和密码,才能进行下一步操作

slider = chrome.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[3]/div/div/div[1]/span')#获取滑块

action = ActionChains(chrome)#创建动作链
action.click_and_hold(slider)#模拟按住滑块不松开
try:
        action.move_by_offset(258,0).perform()#拖动滑块到底,通过浏览器可以获取拖动的距离
except:
    pass
action.release()#释放动作链

login_button = chrome.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[4]/button")#获取登录按钮
login_button.click()#点击登录

sleep(2)
html = chrome.page_source#获取登录后页面信息
choice = chrome.get_cookies()#获取choice
print(choice)
chrome.close()