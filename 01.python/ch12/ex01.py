score = [88, 95, 70, 100, 99]

no = 1
for s in score:
    print(str(no) + "번 학생의 성적:", s)
    no += 1

print("*"*30)

score = [88, 95, 70, 100, 99]

for no in range(len(score)):
    print(str(no+1) + "번 학생의 성적", score[no])


print("*"*30)

race = ['저그', '테란', '프로토스']

list(enumerate(race))

print("*"*30)

score = [88, 95, 70, 100, 99]

for no, s in enumerate(score, 1):
    print(str(no) + "번 학생의 성적 :" , s)