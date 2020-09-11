'''
사람 위치와 목적지 위치가 같을 때 고려해야함, 목적지가 같을 수도 있음
그리고 런타임 걸림
gggggg

6 4 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
1 6 5 4

ans 20
'''

from collections import deque

N, M, F = map(int ,input().split())

arr = [list(map(str, input().split())) for _ in range(N)]

tx, ty = map(int, input().split())
arr[tx-1][ty-1] = 't'

for i in range(1, M+1):
    x1, y1, x2, y2 = map(int, input().split())
    arr[x1-1][y1-1] = 'm' + str(i)
    arr[x2-1][y2-1] = 'g' + str(i)

# for i in range(N):
#     print(arr[i])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_man(tx, ty):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for k in range(4):
        if 0 <= tx+dx[k] < N and 0 <= ty+dy[k] < N:
            if visited[tx+dx[k]][ty+dy[k]] == 0 and arr[tx+dx[k]][ty+dy[k]] != '1':
                q.append([tx+dx[k], ty+dy[k], 1])
                visited[tx+dx[k]][ty+dy[k]] = 1

    while q:
        x, y, c = q.popleft()
        if arr[x][y][0] == 'm':
            selected = [x, y, c]
            while q:
                nx, ny, nc = q.popleft()
                if c < nc:
                    break
                elif c == nc and arr[nx][ny][0] == 'm':
                    if arr[nx][ny][1] < arr[selected[0]][selected[1]][1]:
                        selected = [nx, ny, nc]

            return selected

        else:
            for k in range(4):
                if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                    if visited[x+dx[k]][y+dy[k]] == 0 and arr[x+dx[k]][y+dy[k]] != '1':
                        q.append([x+dx[k], y+dy[k], c+1])
                        visited[x+dx[k]][y+dy[k]] = 1

    return -1, -1, -1

def find_goal(tx, ty):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for k in range(4):
        if 0 <= tx+dx[k] < N and 0 <= ty+dy[k] < N:
            if visited[tx+dx[k]][ty+dy[k]] == 0 and arr[tx+dx[k]][ty+dy[k]] != '1':
                q.append([tx+dx[k], ty+dy[k], 1])
                visited[tx+dx[k]][ty+dy[k]] = 1

    while q:
        x, y, c = q.popleft()
        if arr[x][y] == 'g' + arr[tx][ty][1]:
            return x, y, c
        else:
            for k in range(4):
                if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                    if visited[x+dx[k]][y+dy[k]] == 0 and arr[x+dx[k]][y+dy[k]] != '1':
                        q.append([x+dx[k], y+dy[k], c+1])
                        visited[x+dx[k]][y+dy[k]] = 1
    return -1, -1, -1

ans = 0
while True:
    if ans == M:
        print(F)
        break
    nx, ny, nc = find_man(tx-1, ty-1)
    if nx == -1 and ny == -1 and nc == -1:
        print(-1)
        break
    arr[tx-1][ty-1] = '0'
    if F - nc >= 0:
        F -= nc
        gx, gy, gc = find_goal(nx, ny)
        if gx == -1 and gy == -1 and gc == -1:
            print(-1)
            break
        arr[nx][ny] = '0'
        arr[gx][gy] = 't'
        tx = gx + 1
        ty = gy + 1
        if F - gc >= 0:
            F += gc
            ans += 1
            continue
        else:
            print(-1)
            break
    else:
        print(-1)
        break