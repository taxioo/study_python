list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
list1.extend(list2)
print(list1)   #extend는 원본을 수정해서 확장 / + 기존 리스트를 확장

print(list1 + list2)