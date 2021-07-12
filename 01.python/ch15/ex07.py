f = open("live.txt", 'rt', encoding='utf-8')

f.seek(32,0)

text = f.read()

f.close()

print(text)