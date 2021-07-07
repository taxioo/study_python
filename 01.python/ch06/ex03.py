# #for 문
# 컬렉션의 요소를 하나씩 꺼내 명령 블럭을 실행
# 컬렉션의 모든 요소를 다 사용하면 반복을 끝냄

# for 제어변수 in 컬렉션(값의 모음):
#     명령

for student in [1, 2, 3, 4, 5]:
    print(student, "번 학생의 성적을 처리한다.")

# range(시작, 끝[, 증가값=1])  끝은 포함되지않음


total = 0
for num in range(1, 101):
    total  += num

print('total =', total)


total = 0
for num in range(2, 101, 2):
    total += num

print('total=', total)

for a in range(5):
    print("이 문장을 반복합니다.")


for x in range(1, 51):
    if (x%10) == 0:
        print('+', end='')
    else:
        print('-', end='')
