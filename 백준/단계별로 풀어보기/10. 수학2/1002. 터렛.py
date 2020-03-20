T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    # print(d)

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif d == r1 + r2:
        print(1)
    elif d > r1 + r2:
        print(0)
    elif d < r1 + r2:
        if d + r1 == r2:
            print(1)
        elif d + r2 == r1:
            print(1)
        elif d + r2 < r1:
            print(0)
        elif d + r1 < r2:
            print(0)
        else:
            print(2)