T = int(input())


def f(m, n):
    while(True):
        if m % n == 0:
            return n
        temp = m % n
        m = n
        n = temp



for _ in range(0, T):
    a, b = map(int, input().split())
    c = f(a, b)
    res = a * b // c
    print(res)

