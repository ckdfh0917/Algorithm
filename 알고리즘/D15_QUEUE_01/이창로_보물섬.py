m, n = map(int, input().split())

arr = [input() for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * n for _ in range(m)]
q = []

maxV = 0

def bfs():
    global maxV
    cnt = 0
    minV = 987654321
    while q:
        x, y, cnt = q.pop(0)
        if arr[x][y] == 'L':
            visited[x][y] = True
            for a in range(4):
                if 0 <= x + dx[a] < m and 0 <= y + dy[a] < n:
                    if arr[x + dx[a]][y + dy[a]] == 'L' and not visited[x + dx[a]][y + dy[a]]:
                        q.append([x + dx[a], y + dy[a], cnt+1])
                        visited[x+dx[a]][y+dy[a]] = True
    minV = min(cnt, minV)
    maxV = max(maxV, minV)

for i in range(m):
    for j in range(n):
        visited = [[False] * n for _ in range(m)]
        q = []
        if arr[i][j] == 'L' and not visited[i][j]:
            q.append([i, j, 0])
            bfs()


print(maxV)