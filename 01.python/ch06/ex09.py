def print_dec_star(n):
    for y in range(1, n+1):
        for x in range(y):
            print('*', end='')
        print()

print_dec_star(10)
print()

for _ in range(1,10):
    print('*', end='')
print()