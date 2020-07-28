munja = input()

cnt = 0
for x in munja:
    t = ord(x)
    if t >= 97:
        cnt += t - 96
    else:
        cnt += t - 38

dp = [0] * 10001
dp[0] = 1
dp[1] = 0
def f(n):
    for i in range(2, n):
        if dp[i] == 0:
            k = 2*i
            while k < n:
                dp[k] = 1
                k += i
# print(dp)
# print(cnt)
f(10000)
if cnt == 1:
    print('It is a prime word.')
else:
    if dp[cnt] == 0:
        print('It is a prime word.')
    else:
        print('It is not a prime word.')