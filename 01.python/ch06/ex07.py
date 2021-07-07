dan = 3

#변하지 않는 부분 --> 리터럴 처리
#변하는 부분 --> 변수

# # 변수 변수
# 3 x 1= 3
# 3 x 2= 6
# 3 x 3= 9
# :
# 3 x 9= 27

for s in range(1,10):
    result = 3*s
    print('3 x', s, '=', result)


for dan in range(2, 10): #[2,3,4,5,~9]
    for hang in range(1, 10):
        print(dan, 'x', hang, '=', dan*hang,)
        
    print()