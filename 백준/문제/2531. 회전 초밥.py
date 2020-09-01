N, d, k, c = map(int, input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))

maxV = 0
for i in range(N-k+1):
    temp = sushi[i:i+k]
    temp.append(c)
    temp = set(temp)
    maxV = max(maxV, len(temp))


for i in range(N-k+1, N):
    temp = sushi[i:i+k] + sushi[:i-N+k]
    temp.append(c)
    temp = set(temp)
    maxV = max(maxV, len(temp))

print(maxV)
