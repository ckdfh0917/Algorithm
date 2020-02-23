N = int(input())

dp = [[0 for _ in range(2)] for _ in range(N)]


dp[0][0] = 0
dp[0][1] = 1

for i in range(1,N):
    dp[i][j] = dp[i-1][0] + dp[i-1][1]
    dp[i][j] = dp[i-1][0]

result = dp[N-1][0] + dp[N-1][1]
print(result)