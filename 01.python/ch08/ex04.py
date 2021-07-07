# 슬라이싱
#     문자열[begin:end:step]
#     steip : 음수이면 뒤에서부터 진행

s = "0123456789"
print(s[2:5])
print(s[3:])
print(s[:4])

file_name = "song.mp3"

#file_name이 mp3파일인지 여부 판단

print(file_name[-3:])
print(file_name[-3:] == "mp3")

s_num = "930920"
print("출생년도는 ", s_num[:2])
print("출생월은 ", s_num[2:4])  #end-begin