# .find(str) : str 문자열을 찾아 인덱스 반환, 없으면 -1 반환
# .rfind(str) : 뒤에서 str 문자열을 찾아 인덱스 반환, 없으면 -1 반환
# .index(str) : find()와 동일, 없으면 예외 발생
# .count(str) : str 문자열이 몇번 등장하는지 리턴

s = "python programming"
print(len(s))
print(s.find('o'))
print(s.find('z'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))

file_name = 'test.jpeg'

ix = file_name.find('.')
print(ix)

ext_name = file_name[ix+1:]
print(ext_name)

if ix != -1: # 문자가 있는 경우
    ext_name = file_name[ix+1]
    print(ext_name)
else:  # '.' 문자가 없는 경우
    print('확장자 없음')