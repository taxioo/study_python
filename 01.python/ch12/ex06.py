list1 = ['a', 'b']
list2 = list1
list3 = list1.copy()
import copy
list4 = copy.deepcopy(list1)
print("list1 == list2", list1 is list2)
print("list1 == list3", list1 is list3)
print(list4 is list1)