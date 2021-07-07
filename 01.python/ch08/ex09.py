# 단어 in 문자열 -> bool
# 단어 no in 문자열 -> bool
# .startswith(str) -> bool
# .endswith(str) -> bool

s = "python programing"

print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

name = '홍길동'
if name.startswith('홍'):
    print('홍씨입니다.')

if name.startswith("김"):
    print("김씨입니다.")
else:
    print('그럼 어디 성씨냐')

file = "figure.jpg"
if file.endswith('.jpg'):
    print('jpg 그림 파일입니다.')