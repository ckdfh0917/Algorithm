N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
print(arr)

dp = [0] * N
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]

for i in range(2, N):
    dp[i] = max(dp[0] + arr[i], dp)