R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [-1, 0, 1]
dy = [1, 1, 1]
ans = 0

def dfs(x, y):
    global ans

    if y == C-1:
        ans += 1
        return True

    for k in range(3):
        if 0 <= x+dx[k] < R and 0 <= y+dy[k] < C:
            if visited[x+dx[k]][y+dy[k]] == 0 and arr[x+dx[k]][y+dy[k]] == '.':
                visited[x+dx[k]][y+dy[k]] = 1
                if dfs(x+dx[k], y+dy[k]):
                    return True



for i in range(R):
    dfs(i, 0)

print(ans)