#리스트와 검색 값을 인수로 받아서,
#해당 값이 있는 인덱스를 반환하고,
#검색 값이 없으면 -1을 리턴하는 find_value() 함수를 작성하세요

score = [88, 95, 70, 100, 99, 88, 78, 50]
def find_value(datas, value):
    ix = 0
    for data in datas:
        if data == value: #리스트의 요소값이 검색값과 일치하면
            #ix= data의 ix = 지금까지 몇번 루프를 돌렸느냐
            return ix
            pass
        ix += 1

    print() # for 루프를 다 돌았다는 의미 --> 찾은 값이 리스트에 없음
    return -1   #데이터가 없으면 -1리턴


ix = find_value(score, 88)
print(f'88의 인덱스 {ix}')