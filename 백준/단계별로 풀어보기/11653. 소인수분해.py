N = int(input())

k = 2
res = []
while True:
    #print("N: ", N, " k : ", k)
    if N == 1:
        break

    if N % k == 0:
        res.append(k)
        N //= k
        k = 2
    else:
        k += 1

for r in res:
    print(r)