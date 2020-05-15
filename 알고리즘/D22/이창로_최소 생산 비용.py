T = int(input())

def dfs(v, col):
    global minV
    # print(v, col, sum(v))
    if col == N:
        minV = min(minV, sum(v))
        return
    else:
        for j in range(N):
            if v[j] == 0:
                v[j] = arr[col][j]
                if minV <= sum(v):
                    v[j] = 0
                    continue
                dfs(v, col+1)
                v[j] = 0
    return


for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minV = 12345678901

    visited = [0] * N
    dfs(visited, 0)

    print('#{} {}'.format(test_case, minV))