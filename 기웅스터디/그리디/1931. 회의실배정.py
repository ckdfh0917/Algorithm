N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))

new_lst = sorted(lst, key = lambda x : (x[1],x[0]))

cnt = 0
t = 0

for i in range(N):
    if t <= new_lst[i][0] and new_lst[i][0] == new_lst[i][1]:
        t = new_lst[i][0]
        # print(i,new_lst[i])
        cnt += 1
    elif t < new_lst[i][1] and t <= new_lst[i][0]:
        t = new_lst[i][1]
        # print(i,new_lst[i])
        cnt += 1

print(cnt)