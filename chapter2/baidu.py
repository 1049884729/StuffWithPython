'''
学习webdriver,该脚本打开火狐浏览器，输入百度网址，搜索“Selenium2”的功能
'''
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

'''
百度输入框节点
<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">'''

# driver.find_element_by_xpath("//input[@id='kw']").send_keys("Selenium2")
# driver.find_element_by_id("kw").send_keys("Selenium2")
# driver.find_element_by_css_selector(".s_ipt").send_keys("图片")#通过类定位
# driver.find_element_by_css_selector("#kw").send_keys("图片")#通过id定位
# driver.find_element_by_css_selector("[autocomplete=off]").send_keys("图片")#通过属性定位
# driver.find_element_by_css_selector("[name='wd']").send_keys("图片")#通过属性定位
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("图片")#id 定位

# driver.find_element(By.ID,"kw").send_keys("图片") #使用此方法，需要from selenium.webdriver.common.by import  By
#
# '''百度提交节点
# <input id="su" value="百度一下" class="bg s_btn" type="submit">'''
# driver.find_element_by_id("su").click()

try:
    sreach_windows = driver.current_window_handle
    driver.find_element_by_css_selector("a.lb:nth-child(7)").click()
    # <a class="pass-reglink" href="https://passport.baidu.com/v2/?reg&amp;tt=1514041631093&amp;overseas=undefined&amp;gid=7C60A2B-4878-4FFE-8BAE-3A475F8B4619&amp;tpl=mn&amp;u=https%3A%2F%2Fwww.baidu.com%2F" target="_blank">立即注册</a>
    driver.implicitly_wait(10)  # 弹出框需要时间等待，所以需要添加这个隐形等待
    driver.find_element_by_class_name("pass-reglink").click()
    all_handlers = driver.window_handles
    for handler in all_handlers:
        if handler != sreach_windows:
            driver.switch_to.window(handler)
except BaseException as msg:
    driver.quit()
    print(msg)

sleep(10)
# driver.quit()


class cleanFile(object):
    def __init__(self):
        pass

    def removeWebCacheLog(self):
        for file in os.listdir("./"):
            '''
            删除产生的文件
            '''
            if file.endswith(".log"):
                  os.remove(file)


cleanFile().removeWebCacheLog()
