import copy
T = int(input())

def dfs(node, cnt):
    global maxV
    visited[node] = 1
    maxV = max(maxV, cnt)
    for i in range(1, N+1):
        if tree[node][i] == 1:
            if visited[i] == 0:
                dfs(i, cnt+1)
    visited[node] = 0
    return


for test_case in range(1, T+1):
    N, M = map(int, input().split())    # 정점, 간선

    tree = [[0] * (N+1) for _ in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        tree[x][y] = 1
        tree[y][x] = 1


    maxV = 1
    for i in range(1, N+1):
        visited = [0] * (N+1)
        dfs(i, 1)
    print('#{} {}'.format(test_case, maxV))