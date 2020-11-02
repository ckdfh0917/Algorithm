import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

n = []
for _ in range(N):
    n.append(int(input()))

dp = [[0, 0, 0] for _ in range(N+1)]
dp[1][n[0]-1] = 1

for i in range(2, N+1):
    if n[i-1] == 1:
        dp[i][0] += dp[i-1][0] + 1
        dp[i][1] = dp[i-1][1]
        dp[i][2] = dp[i-1][2]
    elif n[i-1] == 2:
        dp[i][0] = dp[i-1][0]
        dp[i][1] += dp[i-1][1] + 1
        dp[i][2] = dp[i-1][2]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]
        dp[i][2] += dp[i-1][2] + 1

for _ in range(Q):
    a, b = map(int, input().split())
    print(dp[b][0]-dp[a-1][0], dp[b][1]-dp[a-1][1], dp[b][2]-dp[a-1][2])