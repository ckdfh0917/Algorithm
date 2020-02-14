def dfs():
    visited = {i:0 for i in range(V+1)}
    stack = []
    stack.append(start)
    while stack:
        n = stack.pop(0)
        if n == end:
            return 1
        for t in adj[n]:
            if visited[t] == 0:
                stack.append(t)
                n = t
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(1, V+1)}
    # print(adj)
    for i in range(E):
        u,v = map(int,input().split())
        adj[u].append(v)
    print(adj)
    start, end=map(int,input().split())

    print('#{} {}'.format(tc,dfs()))