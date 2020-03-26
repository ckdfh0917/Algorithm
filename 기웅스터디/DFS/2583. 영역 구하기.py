import sys
input = sys.stdin.readline
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

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(a, b):  # 세로, 가로
    global temp
    visited[a][b] = True
    # print('ddddd',a,b)
    for k in range(4):
        if 0 <= a+dy[k] < M and 0 <= b+dx[k] < N:
            if box[a+dy[k]][b+dx[k]] == 0 and not visited[a+dy[k]][b+dx[k]]:
                temp += 1
                dfs(a+dy[k], b+dx[k])
    return


visited = [[0] * N for _ in range(M)]
area = []
temp = 0
cnt = 0
stack = []
for i in range(M):      # 세로
    for j in range(N):  # 가로
        if box[i][j] == 0 and not visited[i][j]:
            cnt += 1
            temp = 1
            y, x = i, j
            visited[y][x] = 1
            while True:
                # print('ddddd',a,b)
                if visited[y][x] == 0:
                    temp += 1
                visited[y][x] = 1
                # for q in range(M):
                #     print(visited[q])
                # print('=================', temp)
                for k in range(4):
                    if 0 <= y + dy[k] < M and 0 <= x + dx[k] < N:
                        if box[y + dy[k]][x + dx[k]] == 0 and visited[y + dy[k]][x + dx[k]] == 0:
                            stack.append([y + dy[k], x + dx[k]])
                if not stack:
                    break
                else:
                    y, x = stack.pop()

            area.append(temp)
area.sort()
print(cnt)
print(' '.join(map(str, area)))