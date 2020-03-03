import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# dp[x] 는 x까지의 연속합 중 최대 값
dp = [numbers[0]] + [0] * (n-1)

for i in range(1,n):
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])
# print(dp)
print(max(dp))
