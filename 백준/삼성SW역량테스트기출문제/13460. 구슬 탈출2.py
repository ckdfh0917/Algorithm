N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
r_visited = [[0] * M for _ in range(N)]
b_visited = [[0] * M for _ in range(N)]

# for i in range(N):
#     print(maze[i])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
minV = 123456891

def dfs(rx, ry, bx, by, cnt):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(cnt, rx, ry, bx, by)
    for i in range(N):
        print(maze[i])
    print('====================')

    global minV
    if maze[rx][ry] == 'O' and maze[bx][by] != 'O':
        minV = min(minV, cnt)
        return

    if r_visited[rx][ry] == 2 and b_visited[bx][by] == 2:
        return
    if r_visited[rx][ry] == 1 and b_visited[bx][by] == 1:
        r_visited[rx][ry] = 2
        b_visited[bx][by] = 2
    else:
        r_visited[rx][ry] = 1
        b_visited[bx][by] = 1

    if minV < cnt:
        return

    for k in range(4):
        print('k', k)
        nrx = rx
        nry = ry
        nbx = bx
        nby = by

        if 0 <= rx+dx[k] < N and 0 <= ry+dy[k] < M:
            nrx = rx+dx[k]
            nry = ry+dy[k]
        if 0 <= bx+dy[k] < N and 0 <= by+dy[k] < M:
            nbx = bx+dx[k]
            nby = by+dy[k]

        if maze[nrx][nry] == '.' or maze[nbx][nby] == '.':
            cnt += 1




            if k == 0 and nrx == nbx:
                pass
            elif k == 1 and nry == nby:
                pass
            elif k == 2 and nrx == nbx:
                pass
            elif k == 3 and nry == nby:
                pass
            else:
                if maze[nrx][nry] == '.':
                    while True:
                        if 0 <= nrx+dx[k] < N and 0 <= nry+dy[k] < M:
                            nrx += dx[k]
                            nry += dy[k]
                        else:
                            break

                        if maze[nrx][nry] == '.':
                            continue
                        elif maze[nrx][nry] == 'O':
                            minV = min(minV, cnt)
                            return
                        else:
                            maze[nrx-dx[k]][nry-dy[k]] = 'R'
                            maze[rx][ry] = '.'
                            nrx -= dx[k]
                            nry -= dy[k]
                            break

                if maze[nbx][nby] == '.':
                    while True:
                        if 0 <= nrx+dx[k] < N and 0 <= nry+dy[k] < M:
                            nbx += dx[k]
                            nby += dy[k]
                        else:
                            break

                        if maze[nbx][nby] == '.':
                            continue
                        elif maze[nbx][nby] == 'O':
                            return
                        else:
                            maze[nbx-dx[k]][nby-dy[k]] = 'B'
                            maze[bx][by] = '.'
                            nbx -= dx[k]
                            nby -= dy[k]
                            break
            r_visited[nrx][nry] = 1
            b_visited[nbx][nby] = 1

            print(cnt, rx, ry, bx, by)
            for i in range(N):
                print(maze[i])
            print('====================')
            dfs(nrx, nry, nbx, nby, cnt+1)

    return



p_r = [0, 0]
p_b = [0, 0]

for i in range(N):
    for j in range(M):
        if maze[i][j] == 'R':
            p_r = [i, j]
        if maze[i][j] == 'B':
            p_b = [i, j]

dfs(p_r[0], p_r[1], p_b[0], p_b[1], 0)
print(minV)