t = int(input())
for q in range(t):
    n, k = map(int, input().split())

    arr = [0] * n

    temp = 0
    temp2 = 0
    for i in range(1,n+1):
        if i * (i-1) // 2 + 1 <= k < (i+1) * (i+2) // 2 + 1:
            temp = i
            p = i * (i-1) // 2 + 1

    # print('t1',temp)
    # print('A',n-temp-1)
    arr[n-temp-1] = 1

    z = k - p
    # print('z',z)
    arr[n-z-1] = 1
    # print(arr)


    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = 'b'
        else:
            arr[i] = 'a'
    print(''.join(arr))
