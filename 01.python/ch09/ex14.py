score = [88, 95, 70, 100, 99, 88, 78, 50]
print("학생수는 %d명 입니다. "%len(score))

max_value = max(score)
max_ix = score.index(max_value)
print(f"최고 점수는 {max_value}점 입니다. 그리고 인덱스는 {max_ix} ")


mini_value = min(score)
mini_ix = score.index(mini_value)
print(f"최소 점수는 {min(score)}점 입니다. 인덱스는 {mini_ix}")

