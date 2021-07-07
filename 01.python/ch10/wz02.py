dic = {'boy':'소년', 'school':'학교', 'book':'책' }

print(dic.get('boy'))
print(dic.get('book'))
print(dic.get('girl'))
print(dic.get('girl', '사전에 없음'))

#False로 해석되는 값 :0, None, '', [], ()
if dic.get('boy'):
    print('찾아보니 있네영')
else:
    print('없어 슈발롬아')


dic = {'boy':'소년', 'school':'학교', 'book':'책' }

if 'student' in dic:
    print('찾아보니 있네영')
else:
    print('없어 슈발롬아')