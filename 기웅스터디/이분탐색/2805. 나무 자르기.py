N, M = map(int, input().split())
trees = list(map(int, input().split()))

max_V = max(trees)
V = max_V
min_V = 0
result = 0
flag = 0
while True:
    take = 0
    if flag == 1:   # up
        min_V = V
        V = (V + max_V) // 2
    elif flag == 0: # down
        max_V = V
        V = (min_V + V) // 2
    # print('a')
    #
    # print('V',V, min_V, max_V)
    for i in range(N):
        if trees[i] - V > 0:
            take += trees[i] - V
        # print('t',take, M)
        if take > M:
            flag = 1    # 더 높이 잘라야 함
            break
    # print('t',take, M)
    if min_V+1 == max_V:
        result = V
        break
    if take < M:  # 더 낮게 잘라야 함
        flag = 0
    elif take == M:
        result = V
        break
print(result)