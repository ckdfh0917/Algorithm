N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited2 = [False] * (N+1)
def BFS(n):
    visited2[n] = True
    Q = [n]
    res_BFS.append(n)
    while Q:
        curr = Q.pop(0)
        for next in lst[curr]:
            if not visited2[next]:
                visited2[next] = True
                Q.append(next)
                res_BFS.append(next)


def DFS(n):
    visited[n] = True
    res_DFS.append(n)
    for i in range(len(lst[n])):
        if visited[lst[n][i]]: continue
        DFS(lst[n][i])

for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

res_BFS = []
res_DFS = []
# 각 정점을 오름차순으로 정렬
for i in range(1, N+1):
    lst[i].sort()

DFS(V)
BFS(V)
print(' '.join(map(str, res_DFS)))
print(' '.join(map(str, res_BFS)))