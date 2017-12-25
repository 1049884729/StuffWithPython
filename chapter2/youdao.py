'''
如果例子运行不成功，需要自己查看元素
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 模拟键盘

from  selenium.webdriver.common.action_chains import ActionChains  # 模拟鼠标

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from time import sleep,ctime

webPage = webdriver.Firefox();
print(ctime())
webPage.implicitly_wait(5)
webPage.get("http://www.youdao.com/")
print(ctime())

try:
    url = webPage.current_url
    print(url)
    element = WebDriverWait(webPage, 5, 0.5).until(ES.presence_of_element_located((By.ID, "translateContent")))

    element.send_keys("hello")
    webPage.find_element_by_id("form").submit()
    title = webPage.title
    print(title)
    url = webPage.page_source
    print(url)
except BaseException as msg:
    print(msg)
    webPage.quit()
    raise BaseException()

sleep(5)
webPage.quit()
print(ctime())


