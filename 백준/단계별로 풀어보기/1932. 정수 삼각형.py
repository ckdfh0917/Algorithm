n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))


dp = [[] * i for i in range(n)]
dp[0].extend(tri[0])
dp[1].append(tri[0][0] + tri[1][0])
dp[1].append(tri[0][0] + tri[1][1])

for i in range(2, n):
    temp = 0
    for j in range(i+1):
        if j == 0:
            dp[i].append(dp[i-1][0]+tri[i][0])
        elif j == i:
            dp[i].append(dp[i-1][-1] + tri[i][-1])
        else:
            dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j])

print(max(dp[n-1]))