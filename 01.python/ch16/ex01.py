balance = 8000

def deposit(money):
    global balance
    balance += money

def inquire():
    print("잔액은 %d원 입니다 ." %balance)

