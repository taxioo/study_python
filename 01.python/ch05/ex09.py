#문제
#사용자로 부터 id와 비밀번호를 입력받아
#userid, password 변수에 저장
#로그인 가능 여부를 판정하고,
#로그인 실패시 그 이유를 출력하세요

print("="*40)
print('로그인.. 사용자 ID와 비밀번호를 입력하세요')
print("="*40)

USER_ID = 'hong'
PASSWORD = 'abcd'
for _ in range(3):
    userid = input('아이디를 입력하세요')
    password = input('비밀번호를 입력하세요')
    print()

    if userid == USER_ID and password == PASSWORD:
        print("정상 로그인되었습니다.")
    else:
        print("로그인에 실패했습니다.")
        if userid != USER_ID:
            print("등록된 이용자가 아닙니다.")
        elif password != PASSWORD:
            print('비밀번호가 다릅니다.')