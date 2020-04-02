T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    temp = []
    for i in range(M):
        temp.append([arr[i], i+1])

    q = []
    for i in range(N):
        q.append(temp.pop(0))

    while q:
        p, k = q.pop(0)
        p //= 2
        if p == 0:
            if temp:
                q.append(temp.pop(0))
        else:
            q.append([p, k])

    print('#{} {}'.format(test_case, k))