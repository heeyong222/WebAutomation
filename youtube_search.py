from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.youtube.com/")

time.sleep(3)

# 검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_name("search_query") # driver = browser

# search 변수에 지정된 곳에 같은 값을 전송
search.send_keys('코딩') # 검색하고싶은 키워드 입력
time.sleep(1)

# search 변수에 저장된 곳에 엔터 입력
search.send_keys(Keys.ENTER)
