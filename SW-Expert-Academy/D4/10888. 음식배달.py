T = int(input())

def select_food(idx):
    global ans

    if 1 in s:
        # print(s)
        t = dfs()
        # print(t)
        ans = min(t, ans)

    for i in range(idx+1, len(foods)):
        s[i] = 1
        select_food(i)
        s[i] = 0
    return

def dfs():
    res = 0
    # print('sss', s)
    for i in range(len(s)):
        if s[i] == 1:
            fx, fy = foods[i]
            res += arr[fx][fy]
    # print('rr', res)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                minV = 1234567890
                # print(foods)
                # print(s)
                for k in range(len(s)):
                    if s[k] == 1:
                        nx, ny = foods[k]
                        temp = abs(i-nx) + abs(j-ny)
                        minV = min(temp, minV)
                        # print(nx, ny, arr[nx][ny], minV)
                res += minV
    return res






for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 1234567890
    visited = [[0] * N for _ in range(N)]

    foods = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2:
                foods.append([i, j])

    s = [0] * len(foods)
    select_food(-1)

    print('#{} {}' .format(test_case, ans))

