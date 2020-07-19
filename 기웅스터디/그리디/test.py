N = int(input())

lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)

new_lst = sorted(lst, key=lambda x: (x[1], x[0]))

cnt = 0
res = []
flag = 0
for i in range(N):
    if not res:
        res.append(new_lst[0])
        flag = new_lst[0][1]
        cnt += 1
    elif flag <= new_lst[i][0]:
        res.append(new_lst[i])
        cnt += 1
        flag = new_lst[i][1]

print(res)

print(cnt)