T = int(input())

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def lcm(a, b):
    return a * b // gcd(a, b)

result = []

for _ in range(0, T):
    M, N, X, Y = map(int, input().split())
    #length = lcm(max(M, N), min(M, N))
    length = lcm(M, N)
    res = -1
    for k in range(0, N):
        x = (X + M * k) // N
        y = (X + M * k) % N
        if y == Y:
            res = X + M * k
            break

    if res > length:
        res = -1
    result.append(res)

for r in result:
    print(r)