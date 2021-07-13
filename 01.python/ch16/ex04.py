class NameCard:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def print(self):
        print(f'{self.name}, {self.email}, {self.phone},  {self.address}')

#addressbook.txt를 읽어서 NameCard의 리스트를 리턴
class AddressBook:
    def __init__(self):
        self.book=[]


    def load(file_name):
        book = []
        with open(file_name, 'rt', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                line = line.split(',') #예 : ['둘리', 'dooli@gamilcom', '010-1111-3333', '경기도 안양시'] / split = 구분하겠따
                # nc = NameCard(line[0], line[1], line[2], line[3])
                nc = NameCard(*line)
                book.append(nc)
        return book

    def save(self, file_name):
        with open(file_name, 'wt', encoding='utf-8') as f:
            for nc in self.book:
                line = f'{nc.name}, {nc.email}, {nc.phone}, {nc.adress}\n'
                f.write(line)

    #사용자로부터 이름, email, phone, 주소 정보를 입력받고,
    #book에 추가하는 매서드
    def add(self):
        name = input('이름 : ')
        email = input(' email : ')
        phone = input('phone : ')
        address = input('주소 : ')
        if True:
            print('로그인 되셨습니다')
        else:
            print('니 아이디도 모르냐')
        
        nc = NameCard(name, email, phone, address)
        self.book.append(nc)
        self.sort()

    def print(self):
        for ix, nc in enumerate(self.book, 1):
            print(f'{ix} )', end ='')   # sep = '  ', end ="n"
            nc.print()

    def sort(self):
        self.book.sort(key=lambda nc: nc.name)
    
    

    # lambda nc: nc.address  #리턴값이 생략 / 키워드 람다(함수로 봐라)

    # book.sort(key=lambda nc: nc.address)
    # print_book(book)

    
