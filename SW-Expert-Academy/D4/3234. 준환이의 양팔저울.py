T = int(input())

def per(idx, new_left, new_right, new_visited):
    global ans
    print(idx, new_left, new_right, new_visited)
    if 0 not in new_visited:
        flag = False
        for i in range(N):
            # print('aa', sum(new_left[:i+1]), 'bb', sum(new_right[:i+1]))
            if sum(new_left[:i+1]) >= sum(new_right[:i+1]):
                flag = True
            else:
                flag = False
                break
        if flag:
            ans += 1
            print('lllllll', new_left, 'rr', new_right)
            return
        else:
            return

    for i in range(N):
        if new_visited[i] == 0:
            # print(new_left[idx])
            if left[i] != 0:
                new_visited[i] = 1
                new_left[idx] = left[i]
                per(idx+1, new_left, new_right, new_visited)
                new_left[idx] = 0
                new_visited[i] = 0

            else:
                new_visited[i] = 1
                new_right[idx] = right[i]
                print('cc', idx, new_right, right)
                per(idx+1, new_left, new_right, new_visited)
                new_right[idx] = 0
                new_visited[i] = 0


def dfs(idx):
    global ans
    for i in range(N):
        if visitied[i] == 0:
            right[i] = k[i]
        else:
            right[i] = 0

    if sum(left) >= sum(right):
        print('qqq', left, right)
        new_left = [0] * N
        new_right = [0] * N
        new_visited = [0] * N
        per(0, new_left, new_right, new_visited)
        return


    for i in range(idx, N):
        if visitied[i] == 0:
            visitied[i] = 1
            left[i] = k[i]
            dfs(i+1)
            left[i] = 0
            visitied[i] = 0



for i in range(1, T+1):
    N = int(input())
    k = list(map(int, input().split()))
    visitied = [0] * N
    left = [0] * N
    right = [0] * N
    ans = 0
    dfs(0)
    print('#{} {}' .format(i, ans))