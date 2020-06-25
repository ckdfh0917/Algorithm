from collections import deque

N = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start_point, fire_point):
    x, y = start_point
    arr[x][y] = '$'
    q = deque()
    q.append([x, y, 0])

    flag_cnt = 1

    while q:
        x, y, cnt = q.popleft()



        if flag_cnt == cnt:
            for _ in range(len(fire_point)):
                f_x, f_y = fire_point.popleft()

                for k in range(4):
                    if 0 <= f_x + dx[k] < h and 0 <= f_y + dy[k] < w:
                        if arr[f_x + dx[k]][f_y + dy[k]] == '.' or arr[f_x + dx[k]][f_y + dy[k]] == '$':
                            arr[f_x + dx[k]][f_y + dy[k]] = '*'
                            f_visited[f_x + dx[k]][f_y + dy[k]] = 1
                            fire_point.append([f_x+dx[k], f_y+dy[k]])
            flag_cnt += 1

        if arr[x][y] != '*':
            arr[x][y] = '$'
            if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                return print(cnt + 1)

        for i in range(4):
            if 0 <= x + dx[i] < h and 0 <= y + dy[i] < w:
                if arr[x + dx[i]][y + dy[i]] == '.' and visited[x + dx[i]][y + dy[i]] == 0:
                    visited[x + dx[i]][y + dy[i]] = 1
                    q.append([x + dx[i], y + dy[i], cnt+1])


    return print('IMPOSSIBLE')


for _ in range(N):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    f_visited = [[0] * w for _ in range(h)]

    start_point = [0, 0]
    fire_point = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                start_point = [i, j]
                visited[i][j] = 1
            if arr[i][j] == '*':
                fire_point.append([i, j])
                f_visited[i][j] = 1

    bfs(start_point, fire_point)


