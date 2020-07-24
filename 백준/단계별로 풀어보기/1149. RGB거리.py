N = int(input())

cnt = 12345678901
home = []
dp = [[0, 0, 0] for _ in range(1000)]

# print(dp)
for _ in range(N):
    r, g, b = map(int, input().split())
    temp = [r, g, b]
    home.append(temp)

dp[0][0] = home[0][0]
dp[0][1] = home[0][1]
dp[0][2] = home[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + home[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + home[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + home[i][2]
# print(dp)
for i in range(N):
    if dp[N-1][i] < cnt:
        cnt = dp[N-1][i]

print(cnt)
