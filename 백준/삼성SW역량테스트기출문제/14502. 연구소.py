from collections import deque
# import copy

N, M = map(int, input().split())

temp = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     print(temp[i])
# print('############################')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    # arr = copy.deepcopy(temp)
    arr = [temp[i][:] for i in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append([i, j])
                visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            if 0 <= x+dx[k] < N and 0 <= y+dy[k] < M:
                if arr[x+dx[k]][y+dy[k]] == 0 and visited[x+dx[k]][y+dy[k]] == 0:
                    arr[x+dx[k]][y+dy[k]] = 2
                    visited[x+dx[k]][y+dy[k]] = 1
                    q.append([x+dx[k], y+dy[k]])
    cnt = 0
    for i in range(N):
        # print(arr[i])
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    # print('#######################')
    # print(cnt)
    return cnt


res = 0

for i in range(N):
    for j in range(M):
        if temp[i][j] == 0:
            temp[i][j] = 1
            for a in range(N):
                for b in range(M):
                    if temp[a][b] == 0:
                        temp[a][b] = 1
                        for c in range(N):
                            for d in range(M):
                                if temp[c][d] == 0:
                                    temp[c][d] = 1
                                    t = bfs()
                                    res = max(res, t)
                                    temp[c][d] = 0
                        temp[a][b] = 0
            temp[i][j] = 0

print(res)
