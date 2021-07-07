def calcrange(begin, end): #begin부터 end까지 합을 구하는 함수
    total = 0
    for num in range(begin, end+1):
        total += num

    print(begin, "~", end, "=", total)

    return total

    
total = calcrange(3,7)
print('시작값', 3, "~끝값", 7, ", 합계는", total)
