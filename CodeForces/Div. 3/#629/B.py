t = int(input())
for q in range(t):
    n, k = map(int, input().split())

    arr = [0] * (n-2) + [1] * 2

    # print('================', q)
    cnt = 1
    while True:
        flag = 0
        # print(arr, cnt)
        if cnt == k:
            # print(arr)
            break

        for i in range(len(arr)-1):
            if arr[i] == 1 and arr[i+1] == 1:
                arr[i] = 0
                arr[i-1] = 1
                arr[i+1] = 0
                arr[-1] = 1
                cnt += 1
                flag = 1
                break
        if flag == 0:
            for i in range(len(arr)-1,-1,-1):
                if arr[i] == 1:
                    arr[i] = 0
                    arr[i-1] = 1
                    cnt += 1
                    break

    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = 'b'
        else:
            arr[i] = 'a'
    print(''.join(arr))
