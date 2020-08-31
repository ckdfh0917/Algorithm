T = int(input())

dp = [0] * 11
def fectorial(n):
    if n == 1:
        dp[1] = 1
    elif n == 2:
        dp[2] = 2
    elif n == 0:
        dp[0] = 1
    else:
        dp[n] = dp[n-1] * n
    return

for i in range(10):
    fectorial(i)

# print(dp)
def dfs(idx, left, right):
    global ans
    # print('left',idx,  left, right, visitied)

    if left * 2 >= sum_k:
        ans += 2 ** (N-idx) * dp[N-idx]
        # print(ans, N-idx, fectorial(N-idx))
        return
    else:
        for i in range(N):
            if visitied[i] == 0:
                visitied[i] = 1
                dfs(idx+1, left+k[i], right)
                if left >= right+k[i]:
                    dfs(idx+1, left, right+k[i])
                visitied[i] = 0


    return



for i in range(1, T+1):
    N = int(input())
    k = list(map(int, input().split()))
    sum_k = sum(k)
    visitied = [0] * N
    ans = 0
    dfs(0, 0, 0)
    print('#{} {}' .format(i, ans))