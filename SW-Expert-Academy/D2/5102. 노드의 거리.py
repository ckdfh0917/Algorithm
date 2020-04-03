T = int(input())

def bfs(s, g):
    q = []
    visited = [False] * (V+1)

    for i in range(V+1):
        if not visited[i] and tree[s][i]:
            q.append([i, 1])
            visited[s] = True

    while q:
        a, cnt = q.pop(0)
        if a == g:
            return cnt

        for i in range(V+1):
            if not visited[i] and tree[a][i]:
                q.append([i, cnt+1])
                visited[a] = True
    return 0

for test_case in range(1, T+1):
    V, E = map(int, input().split())

    tree = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        tree[a][b] = 1
        tree[b][a] = 1
    S, G = map(int, input().split())

    res = bfs(S, G)
    print('#{} {}' .format(test_case, res))