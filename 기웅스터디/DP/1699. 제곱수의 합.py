n = int(input())
aa = [i%10 for i in range(n+1)]
dp = [0] * (n+1)

for i in range(0,n+1):
    dp[i] = i
# print(dp)
temp = 0
tempB = 0
for i in range(2, n+1):
    for j in range(2, i):
        if j * j > i:
            break
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        # print(i, j, dp)
# print('a',aa)
# print('d',dp)
print(dp[n])