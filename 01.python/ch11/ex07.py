def kim():
    temp = "김과장의 함수"       #temp는 이름만 같은 다른 변수
    print(temp)           

def lee():
    temp = 2**10                #temp는 이름만 같은 다른 변수
    return temp

def park(a):
    temp = a*2                  #temp는 이름만 같은 다른 변수
    print(temp)

kim()
print(lee())
park(6)