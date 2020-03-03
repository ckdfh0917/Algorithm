n = int(input())
a, b = map(int, input().split())
m = int(input())

Q = []
lst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

def bfs(start):
    visited[start] = True
    Q = [start, 0]
    while Q:
        curr = Q.pop(0)
        dist = Q.pop(0)
        if curr == b:
            return print(dist)

        for nex in lst[curr]:
            if not visited[nex]:
                visited[nex] = True
                Q.append(nex)
                Q.append(dist+1)

    return print(-1)

bfs(a)
