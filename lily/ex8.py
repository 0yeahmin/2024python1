# 뭐라노
# python 문법 - 프린트, 리스트 같은거 기본적으로 알기
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://time.navyism.com/?host=naver.com")
driver.implicitly_wait(0.5)
while True:
    message=driver.find_element(by=By.ID,value="time_area")
    severtime=message.text
    print(severtime)
    if severtime=="2024년 04월 01일 12시 13분 00초":
        break
print("time over")
time.sleep(10)