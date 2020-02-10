q = int(input())

for test_case in range(1, q + 1):
    N, Q = map(int, input().split())

    result = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            result[j - 1] = i
        # print(result)
    print('#{} '.format(test_case), end='')
    print(' '.join(map(str, result)))
