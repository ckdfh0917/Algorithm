N, M = map(int, input().split())

lst = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(n):
    visited[n] = True
    if lst[n]:
        for i in range(len(lst[n])):
            if not visited[lst[n][i]]:
                dfs(lst[n][i])


for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)