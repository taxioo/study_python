# 1부터 100까지의 수에 합을 구하기
a =1
while a <= 100:
    print(a)
    a += 1

num = 1
total = 0
while num <= 100:
    total += num
    num += 1

print("total =", total)

#1~100까지의 수 중에서 홀수의 합을 구하라

num = 1
total = 0
while num <= 100:
    if num % 2 == 1:
        total += num
    num += 1

print("홀수의 합", total)

# 1~100까지의 수 중에서 3,5의 공배수를 출력하세요


num =1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(num, '은 3과 5의 공배수임')

    num += 1

# 1~100까지의 수에서 홀수의 합을 구하는데
#if 문을 사용하지 않고 구하세요

num = 1
total = 0

while num <= 100:
    total += num
    num += 2

print("홀수의 총합은", total)