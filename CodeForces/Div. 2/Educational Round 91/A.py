T = int(input())

def per(idx, arr):
    print('a', idx, arr, len(arr))
    if len(arr) == 3:
        return arr

    if len(arr) == 1:
        for i in range(idx+1, n):
            if p[idx] < p[i]:
                per(i, arr + [i])

    if len(arr) == 2:
        for i in range(idx+1, n):
            if p[idx] > p[i]:
                per(i, arr + [i])
    return arr

for _ in range(T):
    n = int(input())
    p = list(map(int, input().split()))

    print(n)
    print(p)

    lst = []
    flag = False
    for i in range(n-2):
        print('aaaaai', i)
        lst = per(i, [i])
        print('l', lst)
        if len(lst) == 3:
            flag = True
            break

    if flag:
        print('YES')
        print(' '.join(map(str, lst)))
    else:
        print('NO')