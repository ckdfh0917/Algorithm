T = int(input())

for _ in range(T):
    a, b, n = map(int, input().split())
    cnt = 0
    while True:
        if a > n or b > n:
            break
        if a >= b:
            b += a
        else:
            a += b
        cnt += 1
    print(cnt)