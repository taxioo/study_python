ans = input("결제 하시겠습니까?")

ans = ans.lower() #소문자 변환, upper()대문자로 변환

if ans in ['yes', 'y', 'ok', '예']:
    print("결제를 진행합니다")
else:
    print("결제를 취소합니다")