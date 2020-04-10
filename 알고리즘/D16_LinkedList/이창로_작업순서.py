T = 10

def dfs(y):
    if len(res) == V:
        return
    else:
        tmpA = 0
        for i in range(V+1):
            if tree[i][y] == 1:
                tmpA += 1
        if tmpA == 0:
            for j in range(V+1):
                if tree[y][j] == 1:
                    if y not in res:
                        res.append(y)
                    tree[y][j] = 0
                    dfs(j)
            if y not in res:
                res.append(y)
                return
        return

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    numbers = list(map(int, input().split()))

    tree = [[0] * (V+1) for _ in range(V+1)]

    for i in range(0,E*2,2):
        tree[numbers[i]][numbers[i+1]] = 1

    res = []
    for i in range(V+1):
        cnt = 0
        for j in range(V+1):
            if tree[j][i] == 1:
                cnt += 1
        if cnt == 0:
            for k in range(V+1):
                if tree[i][k] == 1:
                    if i not in res:
                        res.append(i)
                    tree[i][k] = 0
                    dfs(k)
    for i in range(1, V+1):
        if i not in res:
            res.append(i)


    print('#{} '.format(test_case), end='')
    print(' '.join(map(str, res)))
    # print(len(res))