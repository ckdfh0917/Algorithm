n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [0] + [10001] * (k)

coin.sort()

for x in coin:
    for i in range(x,k+1):
        dp[i] = min(dp[i], dp[i - x] + 1)
# print(dp)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])