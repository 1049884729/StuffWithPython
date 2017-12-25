from selenium import webdriver
import os
from time import sleep
# fp=webdriver.FirefoxProfile() #  初始化 下载工具
#
# '''下列属性，只在FrieFox 浏览器有效，可以在浏览器 输入： about:config进行设置'''

"""提供获取cookies的能力"""
driver =webdriver.Firefox()
# driver.get("http://www.youdao.com")
# cookier=driver.get_cookies()
# print(cookier)
# driver.quit()

"""提供执行脚本 javascript的方法"""
# driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("seleniume")
# driver.find_element_by_id("su").click()
#
# sleep(5)
# js="window.scrollTo(100,450);"
# driver.execute_script(js)#执行页面的脚本javascript
# sleep(3)
# driver.quit()

'''截图'''
# driver.get("http://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("e")
# driver.find_element_by_id("su").click()
# sleep(3)
#
# driver.get_screenshot_as_file("/home/xuff/图片/scr.png")
# driver.close()#关闭窗口
# driver.quit()#关闭浏览器

"""验证码识别技术： 可以通过 Python-tesseract：光学字符识别Tesseract OCR的Python封装包"""

import tess


