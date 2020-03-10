def f(n,s):
    global minV
    if n > 12:
        minV = min(minV, s)
        return
    else:
        f(n+1, s+table[n]*d)
        f(n+1, s+m)
        f(n+3, s+m3)
        

T = int(input())
for tc in range(1, 10+1):
    d, m, m3, y = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    minV = y
    f(1, 0)

    print('#{} {}'.format(tc, minV))
