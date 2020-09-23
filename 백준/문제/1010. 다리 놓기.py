T = int(input())


def per():
    pass


for _ in range(T):
    N, M = map(int, input().split())

    mom = 1
    son = 1

    for x in range(M, M-N, -1):
        # print(x)
        mom *= x

    for y in range(1, N+1):
        # print(y)
        son *= y

    res = mom // son
    print(res)