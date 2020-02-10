q = int(input())

for test_case in range(1, q + 1):
    N, K = map(int, input().split())
    print('#{} '.format(test_case), end='')

    k = []
    for i in range(N + 2):
        k += [0]
    list_a = []
    list_a.append(k)
    for i in range(N):
        temp = [0]
        temp += list(map(int, input().split()))
        temp += [0]
        list_a.append(temp)

    list_a.append(k)
    col = 0
    row = 0

    for i in range(1, N + 1):
        for j in range(1, N - K + 2):
            temp_a = 0
            for k in range(K):
                if list_a[i][j + k] == 1:
                    temp_a += 1
                if temp_a == K:
                    if list_a[i][j + k + 1] == 0 and list_a[i][j - 1] == 0:
                        temp_a = 0
                        col += 1
    for j in range(1, N + 1):
        for i in range(1, N - K + 2):
            temp_b = 0
            for k in range(K):
                if list_a[i + k][j] == 1:
                    temp_b += 1
                if temp_b == K:
                    if list_a[i + k + 1][j] == 0 and list_a[i - 1][j] == 0:
                        temp_b = 0
                        row += 1
    result = col + row

    print('{}'.format(result))


