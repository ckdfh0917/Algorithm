N = int(input())

dp = [0] * 41
dp[0] = 0
dp[1] = 1

for i in range(N):
    k = int(input())
    if k == 0:
        print('1 0')
        continue
    for j in range(2, k+1):
        dp[j] = dp[j-1] + dp[j-2]
    print(dp[k-1], dp[k])
