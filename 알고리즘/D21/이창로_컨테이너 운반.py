T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    check_N = [0] * N
    check_M = [0] * M
    res = 0
    for i in range(M):
        for j in range(N):
            if check_M[i] == 0 and check_N[j] == 0 and w[j] <= t[i]:
                check_M[i] = 1
                check_N[j] = 1
                res += w[j]
                break
    print('#{} {}'.format(test_case, res))