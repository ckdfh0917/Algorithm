T = int(input())


def dfs(idx):
    global ans
    print(left, right)
    if 0 not in visitied:
        flag = False
        print('ll', left, 'rr', right)
        for i in range(N):
            # print('aa', sum(left[:i+1]), 'bb', sum(right[:i+1]))
            if sum(left[:i+1]) >= sum(right[:i+1]):

                flag = True
            else:
                flag = False
                break
        if flag:
            ans += 1
            # print('ll', left, 'rr', right)
            return
        else:
            return

    for i in range(N):
        if visitied[i] == 0:
            visitied[i] = 1
            left[idx] = k[i]
            dfs(idx+1)
            left[idx] = 0
            visitied[i] = 0

            visitied[i] = 1
            right[idx] = k[i]
            dfs(idx+1)
            right[idx] = 0
            visitied[i] = 0



for i in range(1, T+1):
    N = int(input())
    k = list(map(int, input().split()))
    visitied = [0] * N
    left = [0] * N
    right = [0] * N
    ans = 0
    dfs(0)
    print('#{} {}'. format(i, ans))