import random
food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

i = random.randrange(len(food))
print( food[i])


import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(food)
random.shuffle(food)
print(food)