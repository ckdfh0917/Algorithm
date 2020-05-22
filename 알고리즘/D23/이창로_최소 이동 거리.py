T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())

    adj = {i: [] for i in range(N)}
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])

    # print(adj)
    INF = 1234567891
    key = [INF] * (N+1)
    key[0] = 0
    cnt = 0
    while cnt < N:
        minV = INF
        # print(key)
        for dist, wt in adj[cnt]:
            # print('dd',dist, wt)

            if key[dist] > key[cnt] + wt:
                key[dist] = key[cnt] + wt

        # print(key)
        cnt += 1
    print('#{} {}' .format(test_case, key[N]))