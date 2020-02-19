N = int(input())
K = N
i = 0
while True:
    if N < 10:
        N = N * 10 + N
    else:
        a = N % 10
        b = N // 10
        c = b + a
        N = a*10 + c%10
    i += 1
    if N == K:
        break
print(i)