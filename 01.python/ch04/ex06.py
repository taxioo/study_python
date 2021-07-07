# 문제 second 변수의 초 값을
# 분:초 로 출력하세요.

seconds = 3150

minute = seconds // 60  # 몫 구하기
seconds = seconds % 60  # 나머지 구하기

print(minute, seconds, sep=(':'))
print(minute, ':', seconds, sep='')

print('현재시간 ', minute, ':', seconds, sep='')

ms = 123456789 # 밀리초
# 1000밀리초 = 1초
# 시:분:초.밀리초
seconds = ms//1000      # 123456초
ms = ms%1000            # 789말리초
print(seconds, ms)

hours = seconds//3600   # 시
minute = (seconds % 3600) // 60 # 분
seconds = seconds %60
print(hours, minute)
print(hours, ':', minute, ':', seconds,'.', ms, sep = '')