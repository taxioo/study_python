def calcstep(begin, end = 1, step = 1):
    total = 0
    for num in range (begin, end +1, step):
        total += num

    return total

print(f"1 ~ 10 = {calcstep(1, 10, 2)}")
print(f"1 ~ 100 = {calcstep(1, 100)}")

print("%s %d"%('hello', 10))