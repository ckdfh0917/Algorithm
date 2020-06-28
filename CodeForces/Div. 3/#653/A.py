t = int(input())

for _ in range(t):
    x, y, n = list(map(int, input().split()))

    temp = n % x
    k = temp - y
    if k >= 0:
        res = n - k
    else:
        res = n - k - x
    print(res)