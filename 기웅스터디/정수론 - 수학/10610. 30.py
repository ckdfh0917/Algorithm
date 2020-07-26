N = input()

dp = [0] * 10
tmp = 0
if '0' not in N:
    pass
else:
    for x in N:
        t = int(x)
        dp[t] += 1
        tmp += int(x)

res = []
if tmp % 3 != 0:
    pass
else:
    for i in range(9, -1, -1):
        k = dp[i]
        while k:
            k -= 1
            res.append(i)

if not res:
    print(-1)
else:
    print(''.join(map(str, res)))