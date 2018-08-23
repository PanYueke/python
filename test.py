#!usr/bin/python
# -*- coding: UTF-8 -*-


from selenium import webdriver
import time
print("Hello, Python!")
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(5)
browser.quit()


