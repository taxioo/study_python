def calcsum(n):   #함수에 종속된 새로운 코드 블럭이 정의된다(들여쓰기)
    total = 0
    for num in range(n+1):
        total += num

    return total  #return = total이라는 결과를 주겠다


print('~4=', calcsum(4))
print('~10=', calcsum(10))

print('abc')

result = calcsum(4)
print(result)

#4까지의 합 출력
#10까지의 합 출력

total = 0
for num in range(4):
    total += num
print(total)

total = 0
for num in range(11):
    total += num
print(total)

result = calcsum(4, 10)
print(result)