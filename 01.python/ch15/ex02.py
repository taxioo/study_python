try:
    f = open("live.txt", "rt", encoding = 'utf-8')
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()


try:
    with open("live.txt", "rt", encoding='utf-8') as f:
        text = f.read()
        print(text)
except Exception as e:
    print(e)