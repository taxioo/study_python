# 리스트[인덱스] <--indexing(1개의 데이터 접근)
# 리스트[begin:end:step] <--slicing(범위로 추출)

score = [88, 95, 70, 100, 99]
print(score[0])
print(score[2])
print(score[-1])

print("="*10)


print(score[2])
score[2] = 55
print(score[2])

