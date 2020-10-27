# 색맹 게임 자동화 div main으로 구분
from selenium import webdriver
from pprint import pprint
import time
from collections import Counter


driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)


start = time.time()

while time.time() - start <= 60:
    try:
        btn = driver.find_element_by_class_name("main")
        btn.click()
    except:
        pass