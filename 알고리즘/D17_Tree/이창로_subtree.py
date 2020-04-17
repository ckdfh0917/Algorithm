T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0] * (max(temp) + 1) for _ in range(max(temp) + 1)]

    for i in range(0, E*2, 2):
        a, b = temp[i], temp[i+1]
        # print(a, b)
        tree[a][b] = 1
    # for i in range(max(temp)+1):
    #     print(tree[i])

    stack = []
    for i in range(max(temp)+1):
        if tree[i][N] == 1:
            stack.append([i, 1])
            tree[i][N] = 0

    cnt = 1
    stack = [N]
    while stack:
        node = stack.pop(0)
        for i in range(max(temp)+1):
            if tree[node][i] == 1:
                cnt += 1
                # print(node, i)
                stack.append(i)
                tree[node][i] = 0
    print('#{} {}' .format(test_case, cnt))