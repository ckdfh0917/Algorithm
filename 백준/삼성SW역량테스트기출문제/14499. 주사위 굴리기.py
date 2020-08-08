N, M, x, y, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

dice = [0] * 7
def move(c):
    # 동쪽
    temp = dice[:]
    if c == 1:
        dice[1] = temp[4]
        dice[2] = temp[2]
        dice[3] = temp[1]
        dice[4] = temp[6]
        dice[5] = temp[5]
        dice[6] = temp[3]
    # 서쪽
    elif c == 2:
        dice[1] = temp[3]
        dice[2] = temp[2]
        dice[3] = temp[6]
        dice[4] = temp[1]
        dice[5] = temp[5]
        dice[6] = temp[4]
    # 북쪽
    elif c == 3:
        dice[1] = temp[5]
        dice[2] = temp[1]
        dice[3] = temp[3]
        dice[4] = temp[4]
        dice[5] = temp[6]
        dice[6] = temp[2]
    # 남쪽
    elif c == 4:
        dice[1] = temp[2]
        dice[2] = temp[6]
        dice[3] = temp[3]
        dice[4] = temp[4]
        dice[5] = temp[1]
        dice[6] = temp[5]

for k in cmd:
    # 동쪽
    if k == 1:
        if y+1 == M:
            continue
        else:
            y += 1
            move(k)
            print(dice[1])
            if arr[x][y] == 0:
                arr[x][y] = dice[6]
            else:
                dice[6] = arr[x][y]
                arr[x][y] = 0
    # 서쪽
    if k == 2:
        if y == 0:
            continue
        else:
            y -= 1
            move(k)
            print(dice[1])
            if arr[x][y] == 0:
                arr[x][y] = dice[6]
            else:
                dice[6] = arr[x][y]
                arr[x][y] = 0
    # 북쪽
    if k == 3:
        if x == 0:
            continue
        else:
            x -= 1
            move(k)
            print(dice[1])
            if arr[x][y] == 0:
                arr[x][y] = dice[6]
            else:
                dice[6] = arr[x][y]
                arr[x][y] = 0
    # 남쪽
    if k == 4:
        if x+1 == N:
            continue
        else:
            x += 1
            move(k)
            print(dice[1])
            if arr[x][y] == 0:
                arr[x][y] = dice[6]
            else:
                dice[6] = arr[x][y]
                arr[x][y] = 0