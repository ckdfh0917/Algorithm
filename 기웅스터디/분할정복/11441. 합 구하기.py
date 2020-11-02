import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

prefix_sum = [0] * (N+1)
prefix_sum[1] = A[0]
for i in range(1, N):
    prefix_sum[i+1] = prefix_sum[i] + A[i]

# print(prefix_sum)
for _ in range(M):
    i, j = map(int, input().split())
    res = prefix_sum[j] - prefix_sum[i-1]
    print(res)