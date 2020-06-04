from collections import deque
T = int(input())

def bfs(v):
    for i in range(len(G[v])):
        dq.append([G[1][i], 2])
        visitied[1] = 1
    while dq:
        a, b = dq.popleft()
        if b > 3:
            return
        if visitied[a] == 0:
            visitied[a] = b
            for i in range(len(G[a])):
                if visitied[G[a][i]] == 0:
                    dq.append([G[a][i],b+1])
    return

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    visitied = [0] * (N+1)
    dq = deque()

    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    bfs(1)
    ans = 0
    for i in range(len(visitied)):
        if visitied[i] == 2 or visitied[i] == 3:
            ans += 1
    print('#{} {}' .format(test_case, ans))