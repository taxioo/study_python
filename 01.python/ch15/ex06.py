FILE_PATH='addressbook.txt'
# 서혁택,taxioo@naver.com, 010-8455-4557, 부산시 수영구
# 고길동, go@gmail.com, 010-111-2222, 서울시 서초구
# 둘리, dooli@gmail.com, 010-1111-3333, 경기도 안양시
# 도우너, douner@naver.com, 010-1111-4444, 경기도 수원시
# 마이콜, mickol@daum.net, 010-1111-5555, 인천광역시


def load_file(file_path):
    book = []
    #파일을 읽어서 book 리스트 구성
    with open("addressbook.txt", 'rt', encoding='utf-8') as f:
        for line in f:
            line = line.strip() # 공백문자 제거
            if not line:
                    continue
            line = line.split(',')

            book.append(line)

    return book



def orderby(x):
    return x[1]
    
def save_book(file_path, book):
    with open(file_path, 'wt', encoding='utf-8') as f:
        for item in book:
            #리스트를 -->str
            line = ','.join(item)
            f.write(line+'\n')

try:
    book = load_file(FILE_PATH)
    # email로 정렬해서 출력하셍.
    #book.sort(key=orderby)
    book.sort(key = lambda x: x[3])
    for item in book:
            print(item)
    #정렬된 book을 파일에 다시 저장하세요
    save_book(FILE_PATH, book)
except Exception as e:
    print(e)
