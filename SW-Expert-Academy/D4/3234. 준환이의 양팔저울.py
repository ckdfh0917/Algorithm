T = int(input())

def per(idx, new_left, new_right, new_visited):
    global ans
    if idx == N:
        # print(idx, new_left, new_right, new_visited)
        ans += 1
        return
    # left 를 보는 것
    for i in range(0, N):
        # print('i', i, new_left, new_right, new_visited , idx)
        if new_visited[i] == 0:
            # print(new_left[idx])
            if left[i] != 0:
                if new_left+left[i] < new_right:
                    continue
                new_visited[i] = 1
                per(idx+1, new_left + left[i], new_right, new_visited)
                new_visited[i] = 0

            else:
                if new_left < new_right + k[i]:
                    continue
                new_visited[i] = 1
                per(idx+1, new_left, new_right + k[i], new_visited)
                new_visited[i] = 0


def dfs(idx):
    global ans
    if sum(left) >= sum(k) - sum(left):
        # print('qqq', left)
        new_visited = [0] * N
        per(0, 0, 0, new_visited)

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
    ans = 0
    dfs(0)
    print('#{} {}' .format(i, ans))