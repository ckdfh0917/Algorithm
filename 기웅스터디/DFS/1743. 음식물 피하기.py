import sys
sys.setrecursionlimit(100000)

N, M, K = map(int, input().split())

lst = [[False] * (M+3) for _ in range(N+3)]
for _ in range(K):
    r, c = map(int, input().split())
    lst[r][c] = True

dx = [-1,0,1,0] # 위 오른 아래 왼
dy = [0,1,0,-1]

visited = [[False] * (M+3) for _ in range(N+3)]

def dfs(i,j):
    global temp
    temp += 1
    # print('b', i,j)
    for k in range(4):
        if 1 <= i+dx[k] <= N and 1 <= j+dy[k] <= M:
            # print('zz', i+dx[k],j+dy[k])
            if lst[i+dx[k]][j+dy[k]] and not visited[i+dx[k]][j+dy[k]]:
                # print('a',i+dx[k],j+dy[k],lst[i+dx[k]][j+dy[k]])
                visited[i+dx[k]][j+dy[k]] = True
                dfs(i+dx[k], j+dy[k])
    return
result = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        temp = 0
        if lst[i][j] and not visited[i][j]:
            visited[i][j] = True
            dfs(i,j)
        result = max(temp, result)

print(result)