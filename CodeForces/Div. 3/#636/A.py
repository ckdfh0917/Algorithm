t = int(input())

for _ in range(t):
    n = int(input())

    candy = 0
    k = 1
    m = 1
    result = 0
    while True:
        m += 2**k
        if n % m == 0:
            result = n // m
            break
        k += 1
    print(result)