#while문
# 조건이 참인 동안 명령 블럭을 실행
#while 조건:
#명령블록
#if 조건은 참이면 한번만 실행하고 다음으로 넘어감
#while은 조건이 참이면 계속 반복 실행, false면 다음으로 넘어감
student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리합니다.", sep = '')
    student += 1
