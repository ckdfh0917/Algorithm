N = int(input())
for _ in range(N):
    a = list(map(int, input().split()))
    num = a.pop(0)

    sum_V = sum(a)
    mid = sum_V / num
    cnt = 0
    for i in a:
        if i > mid:
            cnt += 1
    temp = cnt / num * 100
    result = round(temp,3)
    print(format(result, '.3f'), end='')
    print('%')

