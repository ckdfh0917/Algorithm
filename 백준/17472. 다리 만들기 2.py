N, M = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     print(land[i])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def marking(x, y ,cnt):
    visited[x][y] = 1
    land[x][y] = cnt
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:
            if land[x+dx[i]][y+dy[i]] == 1 and visited[x+dx[i]][y+dy[i]] == 0:
                marking(x+dx[i], y+dy[i], cnt)
    return

cnt = 0
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if land[i][j] == 1:
            if visited[i][j] == 0:
                cnt += 1
                marking(i, j, cnt)

for i in range(N):
    print(land[i])

pq = [0] * (cnt+1)
print(pq)




