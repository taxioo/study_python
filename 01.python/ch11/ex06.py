def kim():
    temp="김과장의 함수"           #지역변수
    print(temp)                    #지역변수

temp = "전역 변수"                 #전역 변수
kim()
print(temp)