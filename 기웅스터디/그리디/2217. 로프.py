N = int(input())
rope = [int(input()) for _ in range(N)]
# print(rope)
minV = min(rope)
maxV = minV*N

rope.sort(reverse=True)

for i in range(1,N+1):
    temp = min(rope[0:i])
    k = temp * (i)
    maxV = max(maxV, k)
print(maxV)