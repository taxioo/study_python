import time

print(time.time())

print('*'*30)

import time

t = time.time()
print(time.ctime(t))

import time

t = time.time()
print(time.localtime(t))

print("*"*30)

import time

now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec) )

print()
print()

import datetime
now = datetime.datetime.now()
print("%d년%d월%d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))