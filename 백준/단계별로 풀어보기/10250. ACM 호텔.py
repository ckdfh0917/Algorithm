T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    x = (N // H) + 1
    y = N % H

    if N % H == 0:
        x -= 1
    # print(y, x)

    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)
    if y == 0:
        y = H
    y = str(y)
    res = y + x
    print(res)