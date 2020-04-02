N = 20
q = []
n, k = 1, 0
q.append([n, k])

m = 1
while N > 0:
    n, k = q.pop(0)
    N -= k
    m += 1
    q.append([n, k+1])
    q.append([m, 0])

    res = n
    print(n, k, N, q)
print(res)