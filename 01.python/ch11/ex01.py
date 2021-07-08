def calcrange(begin, end):
    total = 0
    for num in range(begin, end+1):
        total += num

    return total

print("3 ~ 7 =", calcrange(3, 7))

print('*'*30)

# def intsum(*ints):
# def intsum(*ints, weight): #에러 / 일반 인수 뒤에서만 올수있음
def intsum(weight, *ints):
    print(type(ints))
    print(weight)
    print(ints)

    total = 0
    for num in ints:
        total += num*weight

    return total

print(intsum(1))
print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6 , 2, 9, 7, 5, 8))

