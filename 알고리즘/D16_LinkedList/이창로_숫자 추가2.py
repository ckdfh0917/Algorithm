T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    for _ in range(M):
        idx, k = map(int, input().split())
        numbers.insert(idx, k)
    print('#{} {}' .format(test_case, numbers[L]))
