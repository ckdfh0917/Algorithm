from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    N_list = [0] * 1999999
    N_list[N] = 1
    res = N
    cnt = 0
    minV = 1234567891
    dq = deque()
    dq.append([N, 0])
    while res != M:
        res, cnt = dq.popleft()
        # print(res, cnt)
        if res == M:
            minV = min(minV, cnt)
        elif cnt >= minV:
            break
        else:
            if 0 < res + 1 <= 1000000 and N_list[res+1] == 0:
                dq.append([res + 1, cnt + 1])
                N_list[res+1] = 1
            if 0 < res - 1 <= 1000000 and N_list[res-1] == 0:
                dq.append([res - 1, cnt + 1])
                N_list[res - 1] = 1
            if 0 < res * 2 <= 1000000 and N_list[res*2] == 0:
                dq.append([res * 2, cnt + 1])
                N_list[res*2] = 1
            if 0 < res - 10 <= 1000000 and N_list[res-10] == 0:
                dq.append([res - 10, cnt + 1])
                N_list[res - 10] = 1

    print('#{} {}'.format(test_case, minV))