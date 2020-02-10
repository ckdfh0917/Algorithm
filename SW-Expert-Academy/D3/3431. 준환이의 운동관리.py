q = int(input())

for test_case in range(1,q+1):
    L, U, X = map(int, input().split())
    print('#{} '.format(test_case), end='')
    if L <= X <= U:
        print(0)
    elif X > U:
        print(-1)
    elif X < L:
        print(L-X)