from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 상어의 위치
shark = [0, 0]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark = [i, j]
# 상어의 크기
shark_size = 2
# 상어가 먹은 물고기 수
eat = 0

def bfs(x, y, cnt):
    global eat, shark_size
    q = deque()
    for k in range(4):
        if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
            if arr[x+dx[k]][y+dy[k]] <= shark_size:
                q.append([x+dx[k], y+dy[k], cnt+1])
    while q:
        nx, ny, c = q.popleft()
        if 0 < arr[nx][ny] < shark_size:
            eat += 1
            if eat == shark_size:
                shark_size += 1
                eat = 0
            arr[x][y] = 0
            arr[nx][ny] = 9
            return nx, ny, c
        elif arr[nx][ny] == shark_size or arr[nx][ny] == 0:
            for k in range(4):
                if 0 <= nx+dx[k] < N and 0 <= ny+dy[k] < N:
                    if arr[nx+dx[k]][ny+dy[k]] <= shark_size:
                        q.append([nx+dx[k], ny+dy[k], c+1])
        else:
            return -1, -1, -1


print(bfs(shark[0], shark[1], 0))


