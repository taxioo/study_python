# .append(값) - 리스트의 끝에 값을 추가
# .insert(위치, 값) - 지정한 위치에 값을 삽입

nums = [1, 2, 3, 4]
nums.append(5)
print(nums)

nums.insert(2, 99)
print(nums)

nums.insert(0, 100)
print(nums)

nums.insert(-1, 1000)
print(nums)