import requests
serviceKey='t47wRYsLc5HzV1fQ/kP/4bFaldxsrqNIFaJXuE0Y5LtjBW7F5Bm0BsXfuoT+2Q4+dUA4BV9unLB5tqXT0mkwww=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : serviceKey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
data=response.json()
print(type(data))
print(data['response']['body']['items'][1]['pm10Value'])