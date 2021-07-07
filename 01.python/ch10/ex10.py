print(set('aaabbbccc'))
print(set([12, 34, 56, 78]))
print(set(('홍길동', '고길동', '을지문덕')))
print(set({'boy': '소년', 'school' : '학교'}))
print(set())

asia = {'korea', 'cina', 'japan'}
asia.add('vietnam')
asia.add('korea')
asia.remove('cina')

print(asia)

for c in asia:
    print(c)