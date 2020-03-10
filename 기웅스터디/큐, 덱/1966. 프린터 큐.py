T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # N : 문서의 수
    # M : 궁금한 문서의 위치
    Q = list(map(int, input().split()))
    check = [False] * N
    check[M] = True
    cnt = 0
    while True:
        maxV = max(Q)
        if Q[0] != maxV:
            temp = Q.pop(0)
            Q.append(temp)
            temp = check.pop(0)
            check.append(temp)
        elif Q[0] == maxV:
            Q.pop(0)
            cnt += 1
            if check.pop(0):
                break
        # print(Q)
    print(cnt)