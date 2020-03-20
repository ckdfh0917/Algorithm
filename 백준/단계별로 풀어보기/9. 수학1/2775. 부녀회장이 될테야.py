T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0] * (n+1) for _ in range(k+1)]
    for i in range(n):
        dp[0][i] = i+1

    # print(dp)
    for i in range(1,k+1):
        for j in range(n):
            dp[i][j] = sum(dp[i-1][0:j+1])
    # print(dp)
    print(dp[k][n-1])