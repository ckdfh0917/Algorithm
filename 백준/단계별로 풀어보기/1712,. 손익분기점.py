A, B, C = map(int, input().split())

diff = C - B

if B < C:
    res = A // diff
    res += 1
else:
    res = -1
print(res)