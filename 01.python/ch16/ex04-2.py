class NameCard:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def print(self):
        print(f'{self.name}, {self.email}, {self.phone},  {self.address}')

class AddressBook:
    def __init__(self):
        self.book = []


    def load(self, file_name):
        self.book = []
        with open(file_name, 'rt', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                line = line.split(',') #예 : ['둘리', 'dooli@gamilcom', '010-1111-3333', '경기도 안양시'] / split = 구분하겠따
                # nc = NameCard(line[0], line[1], line[2], line[3])
                nc = NameCard(*line)
                self.book.append(nc)

    def find(self):
        name = input('검색할 이름 :')
        for nc in self.book:
            if name == nc.name:
                nc.print()
                return
        print(f'{name}은 주소록에 없습니다')
        
    def update(self):
        name = input('검색할 이름 :')
        for nc in self.book:
            if name == nc.name:
                nc.print()
                return


    def print(self):
        for ix, nc in enumerate(self.book, 1):
            print(f'{ix})', end ='')    # sep = '  ', end ="n"
            nc.print()

    def sort(self):
        self.book.sort(key=lambda nc : nc.name)


book = AddressBook()

    # #데이터 로드
book.load('addressbook.txt')
    # book.print()

    # #정렬후 저장
    # book.sort()
    # book.print()
    # book.sace('adressbook.txt')

    # #데이터 추가 &저장
    # book.add()
    # book.print()
    # book.sace('adressbook.txt')

book.find()