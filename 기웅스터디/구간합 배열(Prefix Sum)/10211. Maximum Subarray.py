N = int(input())

for _ in range(N):
    k = int(input())
    X = list(map(int, input().split()))
    dp = [0] * k
    dp[0] = X[0]
    for i in range(1, k):
        t1 = dp[i-1] + X[i]
        t2 = X[i]
        dp[i] = max(t1, t2)

    print(max(dp))