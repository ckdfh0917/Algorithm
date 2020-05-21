# 내림차순
a = [[1, 10], [1, 4], [5, 7], [6, 10]]
a.sort(reverse=True)
print(a)

a.sort()
print(a)

a.sort(key=lambda x:(x[0], x[1]))
print(a)

b = sorted(a, key=lambda x:(x[1], x[0]))
print(b)

