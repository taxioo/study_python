def intsum(*ints):

    print(type(ints))
    print(ints)

    total = 0
    for num in ints:
        total += num

    return total

score = [20, 30, 40, 50 ,70]

#print(intsum(scores)) #리스트 1개를 전달하는 호출 --> 가변인수([...],)
print(intsum(*score)) # 펼침 : [20, 30, 40] --> 20, 30, 40
# --> print(intsum(20,30,40))

print(score)  #[x, x, x, ...]
print(*score)  #print(20, 30, 40, 50, 70)