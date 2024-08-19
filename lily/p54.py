menu={"짬뽕":3000,"짜장면":5000,"탕수육":7000}
print(f"오늘이 메뉴는 (menu)")
selected=input("메뉴를 고르세요:::")
if selected in menu:
    print(f"{selected}의 가격은 {menu[selected]}입니다")
else:
    menu[selected]=10000
    print(f"오늘의 메뉴는 {menu}로 갱신되었습니다.")
    
