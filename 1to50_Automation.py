# selenium을 활용한 1to50게임 자동화
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

# 전역 변수
# 현재 찾아야 될 숫자
num = 1
def clickBtn():
    global num
    btn = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for bt in btn:
        print(bt.text, end='\t')
        if bt.text == str(num):
            bt.click()
            print(True)
            num += 1
            return

while num <= 50:
    clickBtn()