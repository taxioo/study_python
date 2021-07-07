dic = {'boy':'소년', 'school':'학교', 'book':'책' }

#문제
#dic의 내용을 key의 사전순으로
#출력하세요.

#key 목록 추출
keys = list(dic.keys())
#keys = dic.keys()

keys.sort()
print(keys)

for x in keys:
    print(x, dic[x])

print(list(dic))   # key를 엘리먼트로하는 리스트로 변환
# list(dic)
# list(dic.keys())  # 가독성이 좋음