n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

coin.sort()
for x in coin:
    for i in range(1,k+1):
        if i % x == 0:
            dp[i] = i // x
V = coin[0]
I = dp[V]
print(V,I)
for i in range(1,k):
    print(I,V)
    if dp[i] > dp[i+1]:
        dp[i] = dp[I] + dp[i-I]
        V = dp[i+1]
        I = i+1
    # elif dp[i] < dp[i-1]:
    #     pass
    else:
        dp[i] = dp[I] + dp[i-I]
    print(dp)
print(dp)
