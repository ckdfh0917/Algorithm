T = int(input())

for _ in range(T):
    l, r, m = map(int, input().split())

    t = r - l

    a = 0
    b = 0
    c = 0
    n = 0
    for j in range(m-t, m+t+1):
        # j = n * a
        # print(j)
        if j == 0:
            continue
        for i in range(l, r+1):
        # i = a
        #     print('i', j, i)
            if j % i == 0:
                a = i
                n = j // i
                if n == 0:
                    continue
                # print('a, n', i, j // i)
                break
        if a != 0:
            break
    # print(n, a)

    temp = m - n*a
    if temp == 0:
        b = c = l
    elif temp > 0:
        b = r
        c = b - temp
    else:
        b = l
        c = b - temp

    print(a, b, c)

    # print('res')