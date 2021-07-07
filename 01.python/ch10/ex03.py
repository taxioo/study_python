# USER_ID = 'kim'
# PASSWORD = '1234'

users ={
    'kim' : '1234',
    'lee' : '12',
    'seo' : 'abc'
}
user_id = input('ID :')
password = input('PASSWORD : ')

if (user_id in users) and (password == users[user_id]):
    print('정상 로그인 되었습니다.')
else:
    print('로그인에 실패하셨습니다.')
    