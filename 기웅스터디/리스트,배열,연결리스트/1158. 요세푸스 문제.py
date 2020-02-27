N, K = map(int, input().split())

lst = [i for i in range(1,N+1)]
res = []
i = 0
a = 0
while True:
    if i == K:
        i = 0
        t = lst.pop(a - 1)
        res.append(t)
    else:
        a += 1

    if a > len(lst):
        a = 1
    if len(lst) == False:
        break

    if lst[a-1] != 0:
        i += 1

    flag = 0
    for j in range(N):
        if lst[j] != 0:
            flag = 0
            break
        flag = 1
    if flag == 1:
        break
# print(res)
res = str(res)
res = res.replace('[', '<')
res = res.replace(']', '>')
print(res)