N = int(input())
num = list(map(int, input().split()))

dp = [0] * (N)
temp = 0
maxV = 0

dp[0] = num[0]
for i in range(N):
    maxV = 0

    for j in range(0, i):
        if num[i] > num[j]:
            maxV = max(maxV, dp[j])
            dp[i] = num[i] + maxV

    if dp[i] == 0:
        dp[i] = num[i]

print(max(dp))