q = int(input())

for test_case in range(1, q + 1):
    result = 0
    print('#{} '.format(test_case), end='')
    N, M = list(map(int, input().split()))

    arr = []
    temp = []
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # print(arr)

    result = 0
    for m in range(N - M + 1):
        for n in range(N - M + 1):
            num = 0
            for i in range(M):
                for j in range(M):
                    num += arr[i + m][j + n]
            if num > result:
                result = num
        # print(num)
    print(result)
