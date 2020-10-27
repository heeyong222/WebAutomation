from selenium import webdriver
import time, re
from urllib.request import urlretrieve

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.twitch.tv/faker/clip/StylishCoyLatteKappaClaus")

time.sleep(3)

# video 테그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
# print[vid_url]

title_element1 = driver.find_element_by_class_name('tw-flex')
title_element2 = title_element1.find_element_by_tag_name('span')
vid_title, vid_date = None, None

for span in title_element2:
    try:
        d_type = span.get_attribute('data-test-selector')
        if d_type == "title":
            vid_title = span.text
        elif d_type == 'date':
            vid_date = span.text
    except:
        pass

urlretrieve(vid_url, vid_title+'_'+vid_date+'.mp4')

driver.close()