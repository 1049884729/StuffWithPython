from selenium import webdriver
import  os
result=os.system("ls -l ")
print(result)
driver=webdriver.Firefox()
driver.get("http:/www.126.com")

driver.implicitly_wait(10)
driver.find_element_by_id("lbNormal").click()
try:
    driver.find_element_by_css_selector(".j-inputtext dlemail").send_keys("jslzsy")
    driver.find_element_by_name("password").send_keys("jiangsulzsy")
    driver.find_element_by_id("dologin").click()
except BaseException as msg:
    print(msg)
    driver.quit()
