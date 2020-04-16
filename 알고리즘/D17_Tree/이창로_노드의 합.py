T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())     # 노드의 개숫, 리프 노드의 개수, 출력할 노드
    temp = []
    arr = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b
    # print(arr)

    for i in range(N, 0, -1):
        if i % 2 == 0:
            if i+1 <= N:
                arr[i//2] = arr[i] + arr[i+1]
            else:
                arr[i//2] = arr[i]

    print('#{} {}'.format(test_case, arr[L]))

