import random #모듈
result='my_number:'
for i in range(3): #0~5까지 6번 반복실행
    num=random.randint(1,6)
    result=f" {i}:{num}"
    print(result)
