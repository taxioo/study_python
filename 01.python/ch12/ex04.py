lambda x: x + 1

def increase(x):
    return x + 1

score = [45, 89, 72, 53, 94]
for s in filter(lambda x: x < 60, score):
    print(s)

score = [45, 89, 72, 53, 94]
for s in map(lambda x: x / 2, score):
    print(s, end = ",")