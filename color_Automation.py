# 색맹 게임 자동화
from selenium import webdriver
from pprint import pprint
import time
from collections import Counter


driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

btn = driver.find_elements_by_xpath('//*[@id="grid"]/div')
def analysis():

    # css 속성 추출
    # print(btn[0].value_of_css_property('background-color'))
    # btn의 색상 리스트
    btn_rgba = [bt.value_of_css_property('background-color') for bt in btn]
    # pprint(btn_rgba)

    # 각각의 색깔이 몇개씩 있는지 판별
    result = Counter(btn_rgba)
    pprint(result)
    # 정답 고르기
    for key, value in result.items():
        if value == 1:
            answer = key
            break
        else:
            answer = None
            print("정답을 찾을 수 없습니다.")

    # 정답 클릭
    # btn_rgba에서 인덱스 값 구하고, 그 인덱스 값으로 btn 인덱스에 접근하여 클릭
    if answer:
        index = btn_rgba.index(answer)
        btn[index].click()


start = time.time()
while time.time() - start <= 60:
    analysis()