T = int(input())

def dfs(i, e, cnt):
    global minV
    if i == N:
        minV = min(minV, cnt)
        return
    elif i < N:
        e = station[i]

    if cnt >= minV:
        return
    else:
        for k in range(e, 0, -1):
            dfs(i+k, e-k, cnt+1)
    return


for test_case in range(1, T+1):
    station = list(map(int, input() .split()))
    N = station[0]
    e = 0
    minV = 12345678901
    cnt = -1
    i = 1
    dfs(i, e, cnt)
    print('#{} {}'.format(test_case, minV))
