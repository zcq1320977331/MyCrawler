from selenium import webdriver

from time import sleep
# 谷歌要配置到script中,火狐配置到python即可
chrome = webdriver.Chrome()
chrome.get("https://login.taobao.com/member/login.jhtml?")#打开测试页面
# chrome.save_screenshot('kuaizhao.png')#保存网页截图图片,当前浏览器屏幕
sleep(2)
baidu_input = chrome.find_elements_by_id('kw')[0]#通过查找页面元素
baidu_input.send_keys('python')
go_button = chrome.find_elements_by_id('su')[0]
go_button.click()
sleep(2)
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#chrome.close(), chrome.quit() 关闭浏览器页面
