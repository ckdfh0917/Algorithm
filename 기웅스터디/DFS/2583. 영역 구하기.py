import sys
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())

box = [[0] * N for _ in range(M)]
# for i in range(M):
#     print(box[i])
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # print('aaaa',x1, y1, x2, y2)
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    for i in range(miny,maxy):
        for j in range(minx,maxx):
            box[i][j] = 1
#             for q in range(M):
#                 print(box[q])
#             print('=================')
# for q in range(M):
#     print(box[q])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(a, b):
    global temp
    if not visited[a][b] and box[a][b] == 0:
        visited[a][b] = True
        # print('ddddd',a,b)
        for k in range(4):
            if 0 <= a+dy[k] < M and 0 <= b+dx[k] < N:
                if box[a+dy[k]][b+dx[k]] == 0 and not visited[a+dy[k]][b+dx[k]]:
                    temp += 1
                    dfs(a+dy[k], b+dx[k])


visited = [[False] * N for _ in range(M)]
area = []
temp = 0
cnt = 0
for i in range(M):      # 세로
    for j in range(N):  # 가로
        if box[i][j] == 0 and not visited[i][j]:
            cnt += 1
            temp = 1
            dfs(i,j)    # 가로, 세로
            area.append(temp)
area.sort()
print(cnt)
print(' '.join(map(str, area)))