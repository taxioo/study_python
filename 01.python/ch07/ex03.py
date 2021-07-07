#lint

def printsum(n):
    total = 0
    for num in range(n+1):
        total += num
    print("~", n, "=", total)

printsum(4)
printsum(10)

#pass
# 아무것도 안하고 넘어감
# # 함수는 반드시 코드 블럭이 있어야함
# -실제 구현을 나중으로 미루고자 할 때 pass지정

def calctotal():
    #나중에 완성할 것
    pass

# 함수명, # 변수명 ---->  코드 블럭에 대한 이름 / 데이터가 일어날 이름
#print_inc_star()   공백대신 슬라이스를 주는방법 snake 표기법 -파이썬에서 권장하는 방법
#PrintIncStar()    단어의 첫글자를 대문자로 표기하는 방법 pascal 표기법
#printIncStar()   첫글자는소문자로 시작하되 다음 단어의 첫글자를 대문자로
#표현하는 방법 Camel 표기법
# print-in-star()   케밥 표기법(파이썬, c언어에서 못사용)


sum = 10
list = 100