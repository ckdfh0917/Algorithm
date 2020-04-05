T = int(input())

def find(minV, maxV):
    global res
    cal = A * abs(maxV - minV) + (N - maxV * minV)
    if minV >= maxV:
        res = min(res, cal)
        return res


for test_case in range(1, T+1):
    N, A, B = map(int, input().split())

    cd = []
    # 공약수 찾기
    for i in range(1, N+1):
        if N % i == 0:
            if cd and cd[-1][1] == i:
                break
            t = N // i
            cd.append([i, t])
    # print(cd)
    res = 1987654321

    x = 0
    while x*x <= N:
        x += 1
    x -= 1
    cal = B*(N-x*x)
    res = min(res, cal)
    # print(cd)
    for i in range(cd[-1][0],cd[-1][1]):
        for j in range(i+1,cd[-1][1]):
            if N - i * j < 0:
                break
            cal = A * abs(i - j) + B*(N-i*j)
            if cal >= 0:
                res = min(res, cal)
                # print(res, i,j)

    for i in range(len(cd)):
        r, c = cd.pop(0)
        cal = A * abs(r-c)
        res = min(res, cal)
    # print(res)


    print('#{} {}' .format(test_case, res))

