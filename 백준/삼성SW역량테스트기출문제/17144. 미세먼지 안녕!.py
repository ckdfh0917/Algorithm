R, C, T = map(int, input().split())

arr = [list(map(int ,input().split()))  for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def f1():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                n = arr[i][j] // 5
                cnt = 0
                for k in range(4):
                    if 0 <= i+dx[k] < R and 0 <= j+dy[k] < C:
                        if arr[i+dx[k]][j+dy[k]] != -1:
                            temp[i+dx[k]][j+dy[k]] += n
                            cnt += 1
                temp[i][j] += arr[i][j] - n * cnt
            elif arr[i][j] == -1:
                temp[i][j] = arr[i][j]

    for i in range(R):
        for j in range(C):
            arr[i][j] = temp[i][j]

def f2():
    up_x, up_y = air
    down_x, down_y = up_x+1, up_y
    temp = 0
    # 오른쪽
    while True:
        if arr[up_x][up_y] == -1:
            temp = arr[up_x][up_y+1]
            arr[up_x][up_y+1] = 0
        else:
            if up_y+1 == C:
                break
            temp2 = arr[up_x][up_y+1]
            arr[up_x][up_y+1] = temp
            temp = temp2
        up_y += 1
    # 위
    while True:
        if up_x-1 == -1:
            break
        temp2 = arr[up_x-1][up_y]
        arr[up_x-1][up_y] = temp
        temp = temp2
        up_x -= 1

    # 왼쪽
    while True:
        if up_y-1 == -1:
            break
        temp2 = arr[up_x][up_y-1]
        arr[up_x][up_y-1] = temp
        temp = temp2
        up_y -= 1
    # 아래
    while True:
        if arr[up_x+1][up_y] == -1:
            break
        temp2 = arr[up_x+1][up_y]
        arr[up_x+1][up_y] = temp
        temp = temp2
        up_x += 1

    # 아래족 바람
    temp = 0
    # 오른쪽
    while True:
        if arr[down_x][down_y] == -1:
            temp = arr[down_x][down_y+1]
            arr[down_x][down_y+1] = 0
        else:
            if down_y+1 == C:
                break
            temp2 = arr[down_x][down_y+1]
            arr[down_x][down_y+1] = temp
            temp = temp2
        down_y += 1
    # 아래
    while True:
        if down_x+1 == R:
            break
        temp2 = arr[down_x+1][down_y]
        arr[down_x+1][down_y] = temp
        temp = temp2
        down_x += 1
    # 왼쪽
    while True:
        if down_y-1 == -1:
            break
        temp2 = arr[down_x][down_y-1]
        arr[down_x][down_y-1] = temp
        temp = temp2
        down_y -= 1
    # 위
    while True:
        if arr[down_x-1][down_y] == -1:
            break
        temp2 = arr[down_x-1][down_y]
        arr[down_x-1][down_y] = temp
        temp = temp2
        down_x -= 1


air = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            air = [i, j]
            break
    if air:
        break

for _ in range(T):
    f1()
    f2()

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)