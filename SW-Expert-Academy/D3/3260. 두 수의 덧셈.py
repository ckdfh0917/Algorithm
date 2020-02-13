q = int(input())

for test_case in range(1, q + 1):
    A, B = map(int, input().split())

    print('#{} {}'.format(test_case, A + B))