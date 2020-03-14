T = int(input())
for _ in range(T):
    n = int(input())

    dp = [0] + [1] + [0] * (45)
    for i in range(1, 47):
        dp[i] = dp[i-1] + i
    # print(dp)

    for i in range(1,47):
        for j in range(1,47):
