from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

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
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    q = deque()
    for k in range(4):
        if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
            if visited[x+dx[k]][y+dy[k]] == 0:
                if arr[x+dx[k]][y+dy[k]] <= shark_size:
                    q.append([x+dx[k], y+dy[k], cnt+1])

    while q:
        qu = list(q)
        # 1) cnt 가 작고 2) x의 값이 작으며 3) y의 값이 작은것
        qu.sort(key=lambda x: (x[2], x[0], x[1]))
        q = deque(qu)
        nx, ny, c = q.popleft()
        visited[nx][ny] = 1
        # 먹을 수 있는 물고기를 만났을 때 -> eat
        if 0 < arr[nx][ny] < shark_size:
            eat += 1
            # 상어의 크기만큼 물고리를 먹었을 때
            if eat == shark_size:
                shark_size += 1
                eat = 0
            arr[x][y] = 0
            arr[nx][ny] = 9
            return nx, ny, c
        # 같은 사이즈의 물고기이거나 0 일때 -> move
        elif arr[nx][ny] == shark_size or arr[nx][ny] == 0:
            for k in range(4):
                if 0 <= nx+dx[k] < N and 0 <= ny+dy[k] < N:
                    if visited[nx+dx[k]][ny+dy[k]] == 0:
                        if arr[nx+dx[k]][ny+dy[k]] <= shark_size:
                            visited[nx+dx[k]][ny+dy[k]] = 1
                            q.append([nx+dx[k], ny+dy[k], c+1])
        else:
            return -1, -1, -1
    return -1, -1, -1

ans = 0
# 아기 상어 초기 위치
x = shark[0]
y = shark[1]
cnt = 0

# 엄마 상어를 찾을 때까지 bfs 반복
while True:
    x, y, cnt = bfs(x, y,cnt)
    # 아기 상어가 더이상 움직일 수 없는 상태
    if x == y == cnt == -1:
        print(ans)
        break
    ans = cnt

