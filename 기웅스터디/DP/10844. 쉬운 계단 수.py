N = int(input())

dp = [0] + [1] * 9
# print(dp)

for _ in range(N-1):
    temp = [0] * 10
    for i in range(10):
        if i == 0:
            temp[i] = dp[i+1]
        elif i == 9:
            temp[i] = dp[i-1]
        else:
            temp[i] = dp[i+1] + dp[i-1]
    dp = temp[:]
    # print(dp)
print(sum(dp) % 1000000000)