# 내림차순
a = [[1, 10], [5, 7], [6, 10]]
a.sort(reverse=True)
print(a)

b = sorted(a, lambda x:(x[1], x[0]))