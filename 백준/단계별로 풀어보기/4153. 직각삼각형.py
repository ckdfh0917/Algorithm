while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    flag = 0
    if a**2 + b**2 == c**2:
        flag = 1
    elif b**2 + c**2 == a**2:
        flag = 1
    elif c**2 + a**2 == b**2:
        flag = 1

    if flag == 1:
        print('right')
    else:
        print('wrong')