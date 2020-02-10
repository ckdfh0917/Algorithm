q = int(input())


def sosu():
    k = [2]
    for i in range(3, 1111, 2):
        cnt = 0
        for j in range(1, i, 2):
            # print(i,j)
            if i % j == 0:
                cnt += 1
            if cnt > 1:
                break
        if cnt == 1:
            k.append(i)
    return k


for test_case in range(1, q + 1):
    N = int(input())

    a = sosu()
    idx = 0
    for i in range(len(a)):
        if a[i] > N:
            idx = i
            break
    cnt = 0
    for i in range(idx, -1, -1):
        for j in range(i, -1, -1):
            if N <= a[i] + a[j]:  # a[i]+a[j]가 N 이상이면 a[j]를 더했을때 무조건 N보다 크므로 continue
                continue
            for k in range(0, j + 1):
                if N < a[i] + a[j] + a[k]:  # N<a[i]+a[j]+a[k] 이면 무조건 N이 될 수 없으므로 break
                    break
                elif N == a[i] + a[j] + a[k]:
                    if a[i] >= a[j] >= a[k]:
                        cnt += 1

    print('# {} {}' .format(test_case, cnt))