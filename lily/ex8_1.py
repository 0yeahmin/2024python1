from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text=f"쿠키런 킹덤"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
driver.implicitly_wait(0.5)
search_button=driver.find_element(by=By.CSS_SELECTOR,value="#search-btn")
# 버튼 엘리먼트를 선택
search_button.click()
driver.implicitly_wait(20)
print("20705 김민서")
crk=driver.find_element(by=By.CSS_SELECTOR,value="._text")
print(crk.text)
time.sleep(10)