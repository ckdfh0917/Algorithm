N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0
def dfs(x, y, sumV, cnt):
    global res
    # print(x, y, sumV, cnt)
    if cnt == 3:
        res = max(res, sumV)
        # print(res, x, y)
        return
    else:
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:
                if visited[x+dx[i]][y+dy[i]] == 0:
                    visited[x+dx[i]][y+dy[i]] = 1
                    dfs(x+dx[i], y+dy[i], sumV+arr[x+dx[i]][y+dy[i]], cnt+1)
                    visited[x+dx[i]][y+dy[i]] = 0

def f():
    global res
    # ㅏ => 왼쪽 위
    for x in range(N-2):
        for y in range(M-1):
            sumV = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y+1]
            res = max(res, sumV)
    # ㅓ => 오른쪽 위
    for x in range(N-2):
        for y in range(M-1, 0, -1):
            sumV = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+1][y-1]
            res = max(res, sumV)
    # ㅗ => 왼쪽 아래
    for x in range(N-1, 0, -1):
        for y in range(M-2):
            sumV = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x-1][y+1]
            res = max(res, sumV)
    # ㅜ => 왼쪽 위
    for x in range(N-1):
        for y in range(M-2):
            sumV = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1]
            res = max(res, sumV)


for i in range(N):
    for j in range(M):
        # print('##########', i, j, '################')
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 0)
        visited[i][j] = 0

f()

print(res)