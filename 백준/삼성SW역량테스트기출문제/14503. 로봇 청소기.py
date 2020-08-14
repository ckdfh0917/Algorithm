import sys
# sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
r, c, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# visited[0] = [1] * M
# visited[N-1] = [1] * M
#
# for i in range(N):
#     visited[i][0] = 1
#     visited[i][M-1] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    if 0 <= d < 2:
        bd = d+2
    else:
        bd = d-2

    c = 0
    for i in range(4):
        if arr[x+dx[i]][y+dy[i]] != 0:
            c += 1
    if c == 4:
        if arr[x + dx[bd]][y + dy[bd]] == 1:
            print('aaa')
            return
    # 1. 현재 위치를 청소한다.
    visited[x][y] = 1
    arr[x][y] = 2
    print(x, y, d)
    for i in range(N):
        print(arr[i])
    print('#################')
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    # 현재 방향을 기준으로 왼쪽 방향 -> d - 1
    if d == 0:
        nd = 3
    else:
        nd = d - 1



    flag = 0
    for i in range(4):
        if nd+i >= 4:
            k = nd+i - 4
        else:
            k = nd+i
        # print(k)
        if arr[x+dx[k]][y+dy[k]] != 0:
            flag += 1
    if flag == 4:
        # d
        if arr[x+dx[bd]][y+dy[bd]] == 1:
            print('끝')
            return
        # c
        else:
            clean(x+dx[bd], y+dy[bd], d)

    # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    if arr[x+dx[nd]][y+dy[nd]] == 0 and visited[x+dx[nd]][y+dy[nd]] == 0:
        clean(x+dx[nd], y+dy[nd], nd)
    # elif arr[x+dx[nd]][y+dy[nd]] == 1 or visited[x+dx[nd]][y+dy[nd]] == 1:
    #     clean(x, y, nd)
    else:
        clean(x, y, nd)

    return

clean(r, c, direction)

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            cnt += 1

print(cnt)