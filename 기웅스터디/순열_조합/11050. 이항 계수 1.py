def f(n, k):
    a = 1
    b = 1
    c = 1
    for i in range(1,n+1):
        a *= i
    for i in range(1,n-k+1):
        b *= i
    for i in range(1,k+1):
        c *= i

    return a // (b * c)

N, K = map(int, input().split())

print(f(N,K))