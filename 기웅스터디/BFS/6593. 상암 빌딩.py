from collections import deque

L = C = R = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [1, -1]

def bfs(start, end):
    x, y, z = start
    e_x, e_y, e_z = end
    visited[z][x][y] = 1
    q = deque()
    for i in range(4):
        if 0 <= x+dx[i] < C and 0 <= y+dy[i] < R and miro[z][x+dx[i]][y+dy[i]] == '.':
            q.append([x+dx[i], y+dy[i], z, 1])  # x, y, z 좌표
            visited[z][x+dx[i]][y+dy[i]] = 1
    for i in range(2):
        if 0 <= z+dz[i] < L and miro[z+dz[i]][x][y] == '.':
            q.append([x, y, z+dz[i], 1])
            visited[z+dz[i]][x][y] = 1
    if not q:
        return 0

    while q:
        new_x, new_y, new_z, cnt = q.popleft()
        if new_x == e_x and new_y == e_y and new_z == e_z:
            return cnt




        for i in range(4):
            if 0 <= new_x + dx[i] < C and 0 <= new_y + dy[i] < R:
                if miro[new_z][new_x + dx[i]][new_y + dy[i]] != '#' and visited[new_z][new_x + dx[i]][new_y + dy[i]] == 0:
                    visited[new_z][new_x + dx[i]][new_y + dy[i]] = 1
                    q.append([new_x + dx[i], new_y + dy[i], new_z, cnt+1])  # x, y, z 좌표
        for i in range(2):
            if 0 <= new_z + dz[i] < L:
                if miro[new_z + dz[i]][new_x][new_y] != '#' and visited[new_z + dz[i]][new_x][new_y] == 0:
                    visited[new_z + dz[i]][new_x][new_y] = 1
                    q.append([new_x, new_y, new_z + dz[i], cnt+1])

    return 0


while True:
    L, C, R = map(int, input().split())
    if L == C == R == 0:
        break

    miro = []
    visited = []
    for i in range(L):
        temp = [list(input()) for _ in range(C)]
        v_temp = [[0] * R for _ in range(C)]

        enter = input()
        miro.append(temp)
        visited.append(v_temp)

    start_point = [0, 0, 0]
    end_point = [0, 0, 0]

    for i in range(L):
        for j in range(C):
            for k in range(R):
                if miro[i][j][k] == 'S':
                    start_point = [j, k, i]
                if miro[i][j][k] == 'E':
                    end_point = [j, k, i]
            if end_point != [0, 0, 0] and start_point != [0, 0, 0]:
                break
        if end_point != [0, 0, 0] and start_point != [0, 0, 0]:
            break

    cnt = bfs(start_point, end_point)
    if cnt == 0:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).' .format(cnt))

