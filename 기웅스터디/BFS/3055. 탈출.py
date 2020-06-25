from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
w_visited = [[0] * C for _ in range(R)]


def bfs(start, end, w):
    e_x, e_y = end.pop()
    x, y, cnt = start.popleft()

    for i in range(4):
        if 0 <= x+dx[i] < R and 0 <= y+dy[i] < C:
            if arr[x+dx[i]][y+dy[i]] == '.' or arr[x+dx[i]][y+dy[i]] == 'D':
                start.append([x+dx[i], y+dy[i], cnt+1])
                visited[x+dx[i]][y+dy[i]] = 1

    water_cnt = 1
    while start:
        x, y, cnt = start.popleft()

        if water_cnt == cnt:
            for i in range(R):
                for j in range(C):
                    if arr[i][j] == '*':
                        w_visited[i][j] = 1
                        for k in range(4):
                            if 0 <= i+dx[k] < R and 0 <= j+dy[k] < C:
                                if w_visited[i+dx[k]][j+dy[k]] == 0:
                                    if arr[i+dx[k]][j+dy[k]] == '.' or arr[i+dx[k]][j+dy[k]] == 'S':
                                        w_visited[i+dx[k]][j+dy[k]] = 1
                                        w.append([i+dx[k], j+dy[k]])

            while w:
                w_x, w_y = w.popleft()
                arr[w_x][w_y] = '*'
            water_cnt += 1

        if arr[x][y] == '*':
            continue

        if arr[x][y] == '.':
            arr[x][y] = 'S'


        if arr[x][y] == 'D':
            return print(cnt)

        for i in range(4):
            if 0 <= x+dx[i] < R and 0 <= y+dy[i] < C:
                if visited[x+dx[i]][y+dy[i]] == 0:
                    if arr[x+dx[i]][y+dy[i]] == '.' or arr[x+dx[i]][y+dy[i]] == 'D':
                        visited[x+dx[i]][y+dy[i]] = 1
                        start.append([x+dx[i], y+dy[i], cnt+1])

    return print('KAKTUS')

end_point = []
water_point = deque()
start_point = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            end_point.append([i, j])
        if arr[i][j] == 'S':
            start_point.append([i, j, 0])
            visited[i][j] = 1
        if arr[i][j] == '*':
            w_visited[i][j] = 1
            water_point.append([i, j])

bfs(start_point, end_point, water_point)
