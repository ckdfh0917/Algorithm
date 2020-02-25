# nCr = n-1Cr + n-1Cr-1

N, K = map(int, input().split())

dp = [[1] * (i+1) for i in range(N+1)]
# print(dp)

def combination(n, k):
    for i in range(2,N+1):     # N
        # print(i)
        for j in range(1,i):   # K
            # print(dp[i-1][j-1], dp[i-1][j])
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007
            # print(dp)
    return dp[n][k]
print(combination(N,K))
