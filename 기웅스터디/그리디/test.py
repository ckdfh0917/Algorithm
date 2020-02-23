import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)

new_lst = sorted(lst, key = lambda x : (x[1], x[0]))
# print('l',lst)
# print('n',new_lst)

#
cls = []
visited = [0] * N
cnt = 0
for j in range(N):
    temp = []
    k = 0
    flag = 0
    for i in range(j, N):
        # print(i, end=' ')

        if not temp and visited[i] == 0:
            temp.append(new_lst[i])
            visited[i] = 1
            k = new_lst[i][1]
        else:
            if visited[i] == 0 and temp[-1][1] <= new_lst[i][0]:   # 이미 정해진 시간표에 끝나는 시간과 새로 정할 시간표에 시작하는 시간 비교
                temp.append(new_lst[i])
                visited[i] = 1
                k = new_lst[i][1]

        # print(visited)
        # print(temp)
        if all(visited):
            flag = 1
            break
    # cls.append(temp)
    cnt += 1
    if flag == 1:
        break


# print(cls)
# print(len(cls), cnt)
print(cnt)