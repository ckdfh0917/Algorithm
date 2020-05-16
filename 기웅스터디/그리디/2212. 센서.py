N = int(input())
K = int(input())

sensor = list(map(int, input().split()))

sum_s = sum(sensor)
p = sum_s // N
for i in range(N):
    sdsd