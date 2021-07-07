# queue : 줄, 줄서다/FIFO(first in fist ou) / 통신에 기본으로 쓰임/ append로 값을 추가하고 pop으로 삭제하는 은행 시스템같은 원리
# 추가 : datas.append(a) .... / 꺼낼떄 a=dats.pop(0) ....
# stack : FILO(first in last out) = LIFO / 접시같은 원리(처음으로 쌓은 접시는 뺄때 마지막에 나옴) / 인터넷처럼 현재 보고있는 화면을 뒤로 돌리면 그전 화면이 나옴
# 추가 : datas.append(a) .... / 꺼낼떄 a=dats.pop() ....
score = [88, 95, 70, 100, 99]
score.append(50)

print('큐', score)
print('큐', score.pop(0))
print('큐', score)

score = [88, 95, 70, 100, 99]
score.append(50)

print('스택', score)
print('스택', score.pop())
print('스택', score)