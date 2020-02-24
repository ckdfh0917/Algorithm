q = int(input())

for k in range(q):
    n, m = map(int, input().split())
    lst_n = [0] + list(map(int, input().split()))
    lst_m = list(map(int, input().split()))
    # print(lst_n)
    i = 0
    # print(k)
    while True:
        flag = 0
        if lst_n[i] in lst_m:
            # print('a', lst_n[i], lst_n[i+1], lst_m)
            if lst_n[i] > lst_n[i+1]:
                lst_n[i], lst_n[i+1] = lst_n[i+1], lst_n[i]
                i = 0
                flag = 1
                # print(lst_n)
        if flag == 0:
            i += 1
        if i == n-1:
            break
    print(lst_n)
    result = 'YES'
    for i in range(n-1):
        if lst_n[i] > lst_n[i+1]:
            result = 'NO'
            break
        else:
            result = 'YES'
    print(result)