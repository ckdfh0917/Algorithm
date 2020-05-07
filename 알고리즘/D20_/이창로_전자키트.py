T = int(input())

def dfs(a, cnt, s):
    global result
    if cnt == N-1:
        s += arr[a][0]
        result = min(result, s)
    else:
        for k in range(N):
            if not visited[k] and k != a:
                visited[a] = True
                dfs(k, cnt+1, s+ arr[a][k])
                visited[a] = False

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 12345678901

    for i in range(1, N):
        visited = [False] * N
        visited[0] = True
        dfs(i, 1, arr[0][i])
    print('#{} {}'.format(test_case, result))