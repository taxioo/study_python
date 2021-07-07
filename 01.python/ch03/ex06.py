a = 5
b = a == 5
print(type(b))
print(b)

A = 6
B = A == 5
print('A==5의 결과', B)
print('A의 결과', A)

# 숫자(정수, 실수), 문자열, 부울린
# ---> Primitive(파이썬 언어를 만든 사람들이 정해놓은 정의)

age = input('나이를 입력하세요')
age = int(age)
result = age > 19
print(result)

print( 'a' > 'b' )
print( 'b' > 'a' )
