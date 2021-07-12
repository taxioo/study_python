
price = 1000

def sale():
    price = 500
    print("sale", id(price))

sale()
print("gloal", id(price))


print("*"*30)

price = 1000

def sale():

    global price
    price = 500

sale()
print(price)