f = open("live.txt", "rt", encoding ='utf-8')
text = ""
line = 1

try:
    with open("live.txt", "rt", encoding ='utf-8') as f:
        while True:
            row = f.readline()
            if not row : break

            text += f'{line} : {row}'
            line += 1
        
except Exception as e:
    print("에러입니당", e)

print(text)

# while True:
#     row = f.readline()
#     if not row: break  # 파일의 끝이면 종료

#     text += f'{line} : {row}' #str(line) + " : " + row
#     line += 1

# f.close()
# print(text)

# print("*"*30)

# f = open("live.txt")