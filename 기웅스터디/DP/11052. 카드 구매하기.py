n = int(input())
dp = [0] + list(map(int, input().split()))

# print('s',dp)

for i in range(1,n+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
# print('e',dp)
print(dp[-1])