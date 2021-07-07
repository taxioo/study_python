s = "짜장 짬뽕 탕수육"
print(s.split())

s2 = "서울->대전->대구->부산"
cities = s2.split("->")
print(cities)

for city in cities:
    print(city)


#split()을 사용해서 파일명 추출
file_path = "\\temp\\test_a\\a.txt"

file_name = file_path.split('\\')[-1]    #-->[ temp, test_a, a.txt ] #indexing
print(file_name)

#file_path에서 파일의 확장명을 추출

file_ext = file_path.split('.')[-1]
print(file_ext)

s3 = '백반'
menu2 = s3.split()
print(menu2)

#split()을 사용해서 파일명 추출
file_name = file_path.split('\\')[-1] #indexing
print(file_name)

#파일의 경로에서 디렉토리의 경로만 추출
dirs = file_path.split('\\')[:-1]  #slicing
print(dirs)  #['', 'temp', 'test_a']

dir_path = '\\'.join(dirs)
print(dir_path)

s = '\\\\'  #\\\\ 역슬래쉬 2개, \\ 역슬래쉬 1개
dir_path = s.join(dirs)
print(dir_path) #\\temp\\test_a

#온드, 습도, 조도
data = '10,60.4,700'
datas = data.split(",")
print(datas)