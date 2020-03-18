l, w, h = map(int, input().split())
n = int(input())

cube = [0] * 20
for _ in range(n):
    a, b = map(int, input().split())
    cube[a] = b

cnt = 0
res = 0

for i in range(19,-1,-1):
    cnt <<= 3
    temp = min(cube[i], (l >> i) * (w >> i) * (h >> i) - cnt)
    cnt += temp
    res += temp

if cnt == l * w * h:
    print(res)
else:
    print(-1)