test_case = 0
while True:
    test_case += 1
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    print('Case {}: '.format(test_case), end='')

    a = V // P
    b = V % P
    if L <= b:
        c = L
    else:
        c = b
    # print(a,b,c)
    result = a*L + c

    print(result)