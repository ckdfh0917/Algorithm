q = int(input())
for test_case in range(1,q+1):
    W, H, N = map(int, input().split())
    des = []
    for i in range(N):
        des.append(list(map(int, input().split())))

    res = 0
    for i in range(N-1):
        if des[i][0] - des[i+1][0] >= 1 and des[i][1] - des[i+1][1] >= 1:
            res -= min(des[i][0] - des[i+1][0], des[i][1] - des[i+1][1])
        elif des[i+1][0] - des[i][0] >= 1 and des[i+1][1] - des[i][1] >= 1:
            res -= min(des[i+1][0] - des[i][0], des[i+1][1] - des[i][1])
        res += abs(des[i][0] - des[i+1][0])
        res += abs(des[i][1] - des[i+1][1])

    print('#{} {}'.format(test_case, res))