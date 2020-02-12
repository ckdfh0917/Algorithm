def sosu(n):
    arr = [False,False] + [True] * (n-2)

    for i in range(2,n):
        if arr[i]:
            for k in range(2*i,n,i):
                arr[k] = False
    for i in range(n):
        if arr[i]:
            print(i, end=' ')
sosu(10**6)