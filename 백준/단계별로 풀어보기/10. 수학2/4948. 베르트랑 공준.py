def sosu(n):
    for i in range(2, n + 1):
        if a[i] == 1:

            for j in range(i * 2, n + 1, i):
                a[j] = 0

while True:
    N = int(input())
    if N == 0:
        break

    a = [0] + [0] + [1] * (2 * N - 1)
    sosu(N*2)
    cnt = 0
    # print(a)
    for i in range(1,len(a)):
        # print('a',i, a[i])
        if N < i <= N * 2 and a[i] == 1:
            cnt += 1

    print(cnt)
