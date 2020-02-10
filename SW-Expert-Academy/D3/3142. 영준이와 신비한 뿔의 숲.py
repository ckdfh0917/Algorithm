q = int(input())

for test_case in range(1, q + 1):
    N, M = map(int, input().split())

    temp = M * 2

    uni = temp - N
    twin = M - uni

    print('#{} {} {}'.format(test_case, uni, twin))