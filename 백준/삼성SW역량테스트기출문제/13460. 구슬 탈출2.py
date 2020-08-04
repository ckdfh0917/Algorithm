import sys
sys.setrecursionlimit(10**9)
# https://juhee-maeng.tistory.com/29

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
        # 위
        if k == 0:
            # 파란공이 더 위
            if rx >= bx:
                if 0 <= bx+dx[k] < N:
                    nbx = bx+dx[k]
                    nrx = rx+dx[k]
                    print('aa')
                    # 파란공 먼저 움직이기
                    while True:
                        print('bb', nbx)
                        if maze[nbx][by] == '.':
                            nbx += dx[k]
                            continue
                        elif maze[nbx][by] == '#':
                            nbx -= dx[k]
                            print('dd', nbx)
                            maze[bx][by] = '.'
                            maze[nbx][by] = 'B'
                            break
                        elif maze[nbx][by] == 'O':
                            return
                    # 빨간공 뒤에 움직이기
                    while True:
                        print('cc')
                        if maze[nrx][ry] == '.':
                            nrx += dx[k]
                            continue
                        elif maze[nrx][ry] == '#':
                            nrx -= dx[k]
                            maze[nrx][ry] = 'R'
                            maze[rx][ry] = '.'
                            break
                        elif maze[nrx][ry] == 'O':
                            minV = min(minV, cnt)
                            return
                    dfs(nrx, ry, nbx, by, cnt+1)
            # 빨간공이 더 위
            else:
                if 0 <= bx+dx[k] < N:
                    nbx = bx+dx[k]
                    nrx = rx+dx[k]
                    # 빨간공 먼저 움직이기
                    while True:
                        if maze[nrx][ry] == '.':
                            nrx += dx[k]
                            continue
                        elif maze[nrx][ry] == '#':
                            nrx -= dx[k]
                            maze[nrx][ry] = 'R'
                            maze[rx][ry] = '.'
                            break
                        elif maze[nrx][ry] == 'O':
                            minV = min(minV, cnt)
                            return
                    # 빨간공 뒤에 움직이기
                    while True:
                        if maze[nbx][by] == '.':
                            nbx += dx[k]
                            continue
                        elif maze[nbx][by] == '#':
                            nbx -= dx[k]
                            maze[bx][by] = '.'
                            maze[nbx][by] = 'B'
                            break
                        elif maze[nbx][by] == 'O':
                            return
                    dfs(nrx, ry, nbx, by, cnt+1)



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