t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    m = {}
    for i in range(n):
        if A[i] % k == 0:
            continue
        temp = A[i] % k
        temp = k - temp


        if m.get(temp) == None:
            m[temp] = 1
        else:
            tmp = m.get(temp)
            m[temp] = tmp + 1
        # print(m)
    # print(m)

    #     print(temp)
    # print(memo)

    maxV = 0
    idx = 0
    for i in m:
        # print(i, m[i])
        if maxV <= m[i]:
            if maxV == m[i]:
                if idx < i:
                    idx = i
            else:
                idx = i
                maxV = m[i]
    #         print(maxV, m[i])
    # print('aa', maxV, idx)
    if maxV == 0:
        res = 0
    else:
        res = (maxV - 1) * k + idx + 1
    print(res)
    # print()