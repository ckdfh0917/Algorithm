import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))

maxV = 0
for i in range(N-k+1):
    temp = set(sushi[i:i+k] + [c])
    maxV = max(maxV, len(temp))





for i in range(N-k+1, N):
    temp = set(sushi[i:i+k] + sushi[:i-N+k] + [c])
    maxV = max(maxV, len(temp))

print(maxV)
