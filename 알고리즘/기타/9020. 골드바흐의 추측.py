T = int(input())

def sosu(n):
    for i in range(2, n+1):
        if a[i] == 1:
            continue
        for j in range(i+i, n+1, i):
            a[j] = 1

for _ in range(T):
    n = int(input())
    a = [1] + [1] + [0] * (n)
    sosu(n)

    v = []
    for i in range(n):
        if a[i] == 0:
            v.append(i)

    minV = 987654321
    a, b = 0, 0
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] + v[j] == n:
                if minV > v[i] - v[j]:
                    a = v[i]
                    b = v[j]

    print(a, b)



