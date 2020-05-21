T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))
    pair = []

    arr = [[0] * (N + 1) for _ in range(N+1)]
    check = [0] * (N+1)
    cnt = 0
    for i in range(0,2*M,2):
        arr[numbers[i]][numbers[i+1]] = 1
        arr[numbers[i+1]][numbers[i]] = 1

    for i in range(1, N+1):
        # print(arr[i])
        if 1 not in arr[i]:
            cnt += 1
    # print(cnt)
    q = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                # print(i,j)
                q.append(j)
                arr[i][j] = 0
                arr[j][i] = 0
        flag = 0
        while q:
            # print(q)
            k = q.pop(0)
            flag = 1
            for z in range(N + 1):
                if arr[k][z] == 1:
                    q.append(z)
                    arr[z][k] = 0
                    arr[k][z] = 0
        if flag == 1:
            cnt += 1

    # print(cnt)

    print('#{} {}' .format(test_case, cnt))
