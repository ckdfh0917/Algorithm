import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sumV = 0
prefix_sum = [0]
for num in numbers:
    sumV += num
    prefix_sum.append(sumV)

for _ in range(M):
    i, j = map(int, input().split())
    res = prefix_sum[j] - prefix_sum[i-1]
    print(res)


