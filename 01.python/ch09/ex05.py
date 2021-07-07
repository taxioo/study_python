score = [
    [90, 70, 80, 100],
    [30, 70, 100, 100],
    [100, 100, 100, 100],
]

total = 0
totalsub=0

for student in score:
    subject_total =0
    for subject in student:
        subject_total += subject
    subjects = len(student)
    average = subject_total/subjects
    print(f'학생 총점 {subject_total}, 평균{subject_total/subjects:.2f}')
    
    total += subject_total
    totalsub += subjects

average = total/totalsub
print(f'전체평균 {average:.2f}')
    

