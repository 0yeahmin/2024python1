import random
#함수정의
def rolling_dice(pip,repeat):
    for r in range(repeat):
        n=random.randint(1,pip)
        print(r,"결과",n)

#함수호출
rolling_dice(6,5)#인수 전달

