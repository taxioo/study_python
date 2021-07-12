try:
    print("네트워크 접속")
    a = 2/0 # 예외가 발생하는 경우
    # a = 2/2 # 예외가발생하지 않는 경우
    print("네트워크 통신 수행")
except Exception as e:
    print("[에러]", e)
finally: #finally가 있으면 except가 생략 가능함 즉 둘중 한개는 무조건 있어야함
    print("접속 해제")

print("작업 완료")