def calcstep(**args):
    print(type(args))
    print(args)
    begin = args.get('begin', 3)
    end = args.get('end', 1)
    step = args.get('step', 1)

    total = 0
    for num in range(begin, end+1, step):
        total += num

    return total

print(f"3 ~ 5 = {calcstep(begin=3, end=5, step=1)}")
print(f"3 ~ 5 = {calcstep(step=1, end=5, begin=3,)}")

dic = {
    'begin' : 1,
    'end' : 100,
    'step' : 2
}
#dict의 펼침 : **사전명
calcstep(**dic) #calstep(begin=1, end=100, step=2)


