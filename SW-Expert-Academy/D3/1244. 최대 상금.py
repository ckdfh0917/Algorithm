def swap(n, cnt):
    num = list(str(n))
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            temp = int(''.join(num))

            if temp not in lst[cnt]:
                lst[cnt].append(temp)

            num[i], num[j] = num[j], num[i]


for tc in range(int(input())):
    N, K = map(int, input().split())
    lst = {i: [] for i in range(K + 1)}

    lst[0].append(N)
    for i in range(1, K + 1):
        for n in (lst[i - 1]):
            swap(n, i)
    # print(lst)
    lst[K].sort(reverse=True)
    print('#{} {}'.format(tc + 1, lst[K][0]))