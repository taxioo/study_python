# .remove(값) : 리스트에서 값을 찾아 첫번째 해당 요소를 제거
# del(리스트[인덱스]) : 지정한 인덱스의 요소를 제거
# [시작:끝] = [] : 지정한 범위의 요소를 제거

score = [88, 95, 70, 100, 99, 88, 78, 50]
score.remove(100)
print(score)

del(score[2])
print(score)

score[1:4]=[]
print(score)

print(50 in score)
print(-100 in score)
#score.remove(-100)
# print(score.find(100))