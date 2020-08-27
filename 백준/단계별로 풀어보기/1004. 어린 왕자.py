T = int(input())

def f(x, y, a, b, c):
    if (x-a)**2 + (y-b)**2 <= c**2:
        return True
    else:
        return False

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        a, b, c = arr[i]
        flag1 = f(x1, y1, a, b, c)
        flag2 = f(x2, y2, a, b, c)
        if flag1 and flag2:
            continue
        elif flag1 and not flag2:
            ans += 1
        elif not flag1 and flag2:
            ans += 1
        else:
            continue
    print(ans)