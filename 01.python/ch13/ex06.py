import calendar as a

print(a.calendar(2018))
print(a.month(2019,1))

import calendar as cal

dates = ["월", "화", "수", "목", "금", "토", "일"]

day = cal.weekday(2021, 8, 15)
print("광복절은 %s요일입니다." %dates[day])