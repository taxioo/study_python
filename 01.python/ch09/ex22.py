names = "이순신", "김유신", "강감찬"
lee, kim, kang = names #unpack
print(lee)
print(kim)
print(kang)


a, b = 12, 34
print(a, b)

a, b = b, a
print(a, b)

a =10
b = 20
c = 30

d = (a, b, c)
print(d)

pos = (10, 20)
print(pos[0]) # x 좌표값
print(pos[1]) # y 좌표값

x, y = pos
print(x)
print(y)