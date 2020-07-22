L, N, rF, rB = map(int, input().split())

xc = []
for _ in range(N):
    xc.append(list(map(int, input().split())))

xc.sort(key=lambda x: (-x[1], x[0]))

res = 0
preX = 0
preT = 0
for i in range(N):
    if rF * xc[i][0] < preT + (xc[i][0] - preX) * rB:
        continue
    res += ((rF * xc[i][0]) - (preT + (xc[i][0] - preX) * rB)) * xc[i][1]
    preT = rF * xc[i][0]
    preX = xc[i][0]

print(res)