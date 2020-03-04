N, M = map(int,input().split())

lst = []
for _ in range(N):
    lst.append(input().split())
# for i in range(N):
#     print(lst[i])
# print(lst[0][0][0])
# print(lst[1])
q = []
visited = [[False] * M for _ in range(N)]
def bfs(i, j):
    cnt = 1
    q.append(i)
    q.append(j)
    q.append(cnt)
    visited[i][j] = True

    while q:
        tempA = q.pop(0)    # i
        tempB = q.pop(0)    # j
        cnt = q.pop(0)
        if tempA == (N-1) and tempB == (M-1):
            return print(cnt)
        if tempA+1 < N:     # 아래가 길이면
            if lst[tempA + 1][0][tempB] == '1':
                if not visited[tempA+1][tempB]:
                    q.append(tempA+1)
                    q.append(tempB)
                    q.append(cnt+1)
                    visited[tempA+1][tempB] = True
        if tempB+1 < M and lst[tempA][0][tempB+1] == '1':      # 오른쪽이 길이면
            if not visited[tempA][tempB+1]:
                q.append(tempA)
                q.append(tempB+1)
                q.append(cnt + 1)
                visited[tempA][tempB+1] = True
        if tempA-1 >= 0 and lst[tempA-1][0][tempB] == '1':       # 위가 길이면
            if not visited[tempA - 1][tempB]:
                q.append(tempA-1)
                q.append(tempB)
                q.append(cnt + 1)
                visited[tempA-1][tempB] = True
        if tempB-1 >= 0 and lst[tempA][0][tempB-1] == '1':       # 왼쪽이 길이면
            if not visited[tempA][tempB-1]:
                q.append(tempA)
                q.append(tempB-1)
                q.append(cnt + 1)
                visited[tempA][tempB-1] = True

bfs(0,0)
