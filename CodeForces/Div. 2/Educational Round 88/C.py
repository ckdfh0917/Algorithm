q = int(input())
for _ in range(q):
    h, c, t = map(int, input().split())

    res = h
    s = h
    cnt = 1
    minV = 1234567891
    pre = 'h'
    now = 'h'
    # print(res)
    while res != t:
        cnt += 1
        if res < t:
            s += h
            res = s / cnt
            pre = now
            now = 'h'
        elif res > t:
            s += c
            res = s / cnt
            pre = now
            now = 'c'

        # print(res)
        if pre == now:
            cnt -= 1
            break
    print(cnt)
    # print('======')