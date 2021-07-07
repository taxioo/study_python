dic = {'boy':'소년', 'school':'학교', 'book':'책' }

print(dic.keys())
print(dic.values())
print(dic.items())


#순회 : 루프를 통해서 콜렉션의 데이터를 모두 처리하는 것
#사전 순회 방법1 : .keys
keylist = dic.keys()
for key in keylist:
    print(key, dic[key])


print()
for key in dic.keys():
    print(key, dic[key])

#사전 순회 방법 2: .items()
for item in dic.items():
    print(item, item[0], item[1])

print('*'*30)

for key, value in dic.items(): #unpac: key, value = (key, value)
    print(key, value)

print('*'*30)
#사전 순회 방법3 (방법1과 동일)
for x in dic:
    print(x, dic[x])