numPC = int(input())
n = int(input())

arr = [[0] * (numPC+1) for _ in range(numPC+1)]
visited = [0] * (numPC+1)

for _ in range(n):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1


def dfs(x):
    global cnt
    for i in range(numPC+1):
        if arr[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
            cnt += 1

cnt = 0
visited[1] = 1
dfs(1)
print(cnt)