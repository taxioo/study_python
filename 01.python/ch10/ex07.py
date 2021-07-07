dic = {'boy':'소년', 'school':'학교', 'book':'책' }
dic2 = {
    'student': '학생',
    'teacher': '선생님',
    'book': '서적'
}

#dic, dic2 원본 유지
#새로운 사전으로 dic, dic2를 merge하세요.
l1 = []
dic3 = {}

dic3.update(dic)
dic3.update(dic2)

print(dic)
print(dic2)
print(dic3)

print('*'*30)
dic1_1 = list(dic)
dic2_2 = list(dic2)
dic3 = (dic1_1 + dic2_2)
print(dic3)

# dic.update(dic2)
# print(dic)

# print(dic+dic2)  #에러
# #debut = 벌레를 제거