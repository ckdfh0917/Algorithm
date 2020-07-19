N = int(input())

munja = []
for _ in range(N):
    munja.append(input())

lst = [[] for _ in range(51)]

for x in munja:
    lst[len(x)].append(x)

# print(lst)
for i in range(51):
    lst[i] = list(set(lst[i]))
    lst[i].sort()

# print(lst)
for i in range(51):
    if lst[i]:
        for j in range(len(lst[i])):
            print(lst[i][j])