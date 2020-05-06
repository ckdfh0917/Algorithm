T = int(input())

def dfs(x, y, cnt):
    global res
    cnt += arr[x][y]
    # print(x, y, cnt)
    if x == N - 1 and y == N - 1:
        res = min(res, cnt)
    elif res < cnt:
        return
    else:
        if x+1 < N:
            dfs(x+1, y, cnt)
        if y+1 < N:
            dfs(x, y+1, cnt)


for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 1234567891
    cnt = 0
    dfs(0, 0, 0)
    print('#{} {}' .format(test_case, res))

