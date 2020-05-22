T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        n = list(map(int, input().split()))
        arr[n[0]][n[1]] = n[2]
        arr[n[1]][n[0]] = n[2]

    # for i in range(V+1):
    #     print(arr[i])
    # print('aaaaaaaaaaaaaaa')
    INF = float('inf')
    mst = [False] * (V+1)
    key = [INF] * (V+1)
    p = [-1] * (V+1)

    cnt = 0
    result = 0
    key[0] = 0
    while cnt < V+1:
        minV = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and key[i] < minV:
                minV = key[i]
                u = i
        mst[u] = True
        result += minV
        cnt += 1
        # print('a', mst)
        # print('b', result)
        # print('d', key)
        for w in range(V+1):
            if arr[u][w] > 0 and not mst[w] and key[w] > arr[u][w]:
                key[w] = arr[u][w]
                p[w] = u
    #     print('c', key)
    #     print('zzzzzzzzzzz')
    # print(key)
    # print(p)
    print('#{} {}'.format(test_case, result))
    # print('=========================')