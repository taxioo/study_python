score = [88, 95, 70, 100, 99]

score.sort()
print(score)

score.reverse()
print(score)

score = [88, 95, 70, 100, 99]

score.sort(reverse=True)
print(score)

country = ["korea", "Japan", "CHINA"]

country.sort()
print(country)

country.sort(key = str.lower)
print(country)