N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if lst[i][j] != 0 and lst[i][j] != 6:
            cctv.append([lst[i][j], i, j])

# print(cctv)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def one(x, y, d, arr):
    nx = x+dx[d]
    ny = y+dy[d]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d]
            ny += dy[d]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d]
                ny += dy[d]


def two(x, y, d, arr):
    nx = x+dx[d]
    ny = y+dy[d]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d]
            ny += dy[d]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d]
                ny += dy[d]

    nx = x-dx[d]
    ny = y-dy[d]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx -= dx[d]
            ny -= dy[d]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx -= dx[d]
                ny -= dy[d]


def three(x, y, d, arr):
    nx = x+dx[d]
    ny = y+dy[d]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d]
            ny += dy[d]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d]
                ny += dy[d]

    nx = x+dx[d-1]
    ny = y+dy[d-1]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d-1]
            ny += dy[d-1]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d-1]
                ny += dy[d-1]


def four(x, y, d, arr):
    nx = x+dx[d]
    ny = y+dy[d]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d]
            ny += dy[d]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d]
                ny += dy[d]

    nx = x+dx[d-1]
    ny = y+dy[d-1]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d-1]
            ny += dy[d-1]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d-1]
                ny += dy[d-1]


    nx = x+dx[d-2]
    ny = y+dy[d-2]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[d-2]
            ny += dy[d-2]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[d-2]
                ny += dy[d-2]


def five(x, y, arr):
    nx = x+dx[0]
    ny = y+dy[0]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[0]
            ny += dy[0]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[0]
                ny += dy[0]

    nx = x+dx[1]
    ny = y+dy[1]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[1]
            ny += dy[1]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[1]
                ny += dy[1]


    nx = x+dx[2]
    ny = y+dy[2]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[2]
            ny += dy[2]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[2]
                ny += dy[2]


    nx = x+dx[3]
    ny = y+dy[3]
    while 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            arr[nx][ny] = '#'
            nx += dx[3]
            ny += dy[3]
        else:
            if arr[nx][ny] == 6:
                break
            else:
                nx += dx[3]
                ny += dy[3]



def cal(tmp, cnt):
    global ans
    if cnt == L:
        count_zero = 0
        for i in range(N):
            # print(tmp[i])
            for j in range(M):
                if tmp[i][j] == 0:
                    count_zero += 1
        # print('###################')
        ans = min(ans, count_zero)
        return
    c, x, y = cctv[cnt]

    if c == 1:
        for k in range(4):
            temp = [tmp[i][:] for i in range(N)]
            one(x, y, k, temp)
            cal(temp, cnt+1)
    elif c == 2:
        for k in range(2):
            temp = [tmp[i][:] for i in range(N)]
            two(x, y, k, temp)
            cal(temp, cnt+1)
    elif c == 3:
        for k in range(4):
            temp = [tmp[i][:] for i in range(N)]
            three(x, y, k, temp)
            cal(temp, cnt+1)
    elif c == 4:
        for k in range(4):
            temp = [tmp[i][:] for i in range(N)]
            four(x, y, k, temp)
            cal(temp, cnt+1)
    else:
        temp = [tmp[i][:] for i in range(N)]
        five(x, y, temp)
        cal(temp, cnt+1)

    return

L = len(cctv)
ans = 123457890
cal(lst, 0)
print(ans)