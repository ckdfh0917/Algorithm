T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    # N명의 사람이 자격
    # M초의 시간을 들이면 K개의 붕어빵을 만들 수
    a = list(map(int, input().split()))

    a.sort()
    bread = 0
    t = 0
    flag = 0
    cnt = 0
    while True:
        if t != 0 and t % M == 0:
            bread += K
        # print(t, bread, cnt)

        for i in range(N):
            if a[i] == t:
                bread -= 1
                cnt += 1

                if bread < 0:
                    flag = 1
                    break

                if cnt == N:
                    flag = 2
                    break
        if flag == 2 or flag == 1:
            break



        t += 1

    print('#{} '.format(test_case), end='')
    if flag == 1:
        print('Impossible')
    elif flag == 2:
        print('Possible')