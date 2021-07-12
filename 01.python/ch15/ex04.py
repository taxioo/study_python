try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        while True:
            rows = f.readlines()
            for row in rows:
                print(row, end ='')
except Exception as e:
    print('에러입니당', e)

