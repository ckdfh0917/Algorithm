T = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    visited[x][y] = True
    q.append([x,y,0])
    while q:
        x, y, cnt = q.pop(0)
        if arr[x][y] == 3:
            return cnt-1
        for k in range(4):
            if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N and arr[x+dx[k]][y+dy[k]] != 1:
                if not visited[x+dx[k]][y+dy[k]]:
                    visited[x+dx[k]][y+dy[k]] = True
                    q.append([x+dx[k], y+dy[k], cnt+1])
    return 0

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
                break
    q = []
    visited = [[False] * N for _ in range(N)]
    print('#{} ' .format(test_case), end='')
    print(bfs(x, y))
