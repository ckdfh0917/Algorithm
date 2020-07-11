t = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcd(a, b):
    return a * b // gcd(a, b)

def f(n):
    arr = []
    for i in range(n-2, 0, -2):
        if n % i == 0:
            arr.append(i)
            break
    return arr

for _ in range(t):
    n = int(input())
    minV = 1234567891
    res = [0, 0]
    if n % 2 == 1:
        new = f(n)
        # print(new)
        for i in new:
            # print(n-i, i, (n-i) % i)
            if (n-i) % i != 0:
                continue
            temp = lcd(i, n-i)
            if minV > temp:
                minV = temp
                res = [i, n-i]
    else:
        res = [n//2, n//2]
    print(' '.join(map(str, res)))