import requests
from bs4 import BeautifulSoup
url=f"https://time.navyism.com/?host=www.naver.com"
response=requests.get(url)
# print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
result=soup.find("div", onclick=f"dayNameControl()")
print(result)