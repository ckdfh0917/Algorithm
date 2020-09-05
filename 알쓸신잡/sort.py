# 내림차순
a = [[1, 10], [1, 4], [5, 7], [6, 10]]
a.sort(reverse=True)
print(a)  # [[6, 10], [5, 7], [1, 10], [1, 4]]

a.sort()
print(a)  # [[1, 4], [1, 10], [5, 7], [6, 10]]

a.sort(key=lambda x: (x[0], x[1]))
print(a)  # [[1, 4], [1, 10], [5, 7], [6, 10]]

b = sorted(a, key=lambda x: (x[1], x[0]))
print(b)  # [[1, 4], [5, 7], [1, 10], [6, 10]]

