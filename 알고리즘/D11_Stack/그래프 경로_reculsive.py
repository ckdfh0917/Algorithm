def dfs(n):
    if n == end:
        return 1
    else:
        for t in adj[n]:
            if visited[t] == 0:
                visited[t] = 1
                if dfs(t) == 1:
                    return 1
        return 0


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    visited = {i:0 for i in range(V+1)}     # 방문 표시
    adj = {i: [] for i in range(1, V+1)}    #{정점: [인접정점들], 정점2:[인접정점들]}
    # print(adj)
    for i in range(E):
        u,v = map(int,input().split())
        adj[u].append(v)
    print(adj)
    start, end=map(int,input().split())

    print('#{} {}'.format(tc,dfs(start)))