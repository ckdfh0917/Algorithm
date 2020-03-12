q = int(input())
for _ in range(q):
    n = int(input())
    t = list(map(int, input().split()))

    minV = min(t)
    flag = 0
    for i in range(n):
        t[i] -= minV
        if t[i] % 2 == 1:
            flag = 1
            break
    if flag == 0:
        print('YES')
    else:
        print('NO')