N = int(input())
K = int(input())

arr = [[0]*(N+1) for _ in range(N+1)]
arr[1][1] = -1
for _ in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1

L = int(input())
cmd = []
for _ in range(L):
    cmd.append(list(map(str, input().split())))

sx = sy = ex = ey = 1
def move(v):
    global apple
    dx = v[0]
    dy = v[1]
    # print('move', dx, dy, sx+dx, sy+dy)
    if 0 < sx+dx < N+1 and 0 < sy+dy < N+1:
        # 사과가 없을 때
        if arr[sx+dx][sy+dy] == 0:
            # print('사과 X')
            # print(sx+dx, sy+dy, ex, ey)
            arr[sx+dx][sy+dy] = -1
            arr[ex][ey] = 0
            return 1
        # 사과가 있을 때
        elif arr[sx+dx][sy+dy] == 1:
            # print('사과 O')
            arr[sx+dx][sy+dy] = -1
            apple += 1
            return 2
        elif arr[sx+dx][sy+dy] == -1:
            return False
    else:
        return False

# 뱀의 머리와 꼬리의 방향성을 시간에 따라 나타냄
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = [[] for _ in range(N*N+1)]

q = 0
t = 0
for x in cmd:
    X = int(x[0])
    C = x[1]
    while q < X:
        direction[q] = d[t]
        q += 1
    if C == 'L':
        if t == 0:
            t = 3
        else:
            t -= 1
    elif C == 'D':
        if t == 3:
            t = 0
        else:
            t += 1

while q < N*N+1:
    direction[q] = d[t]
    q += 1

cnt = 0
apple = 0

while True:
    q = move(direction[cnt])
    sx += direction[cnt][0]
    sy += direction[cnt][1]
    # 사과가 없을 때
    if q == 1:
        ex += direction[cnt-apple][0]
        ey += direction[cnt-apple][1]
    # 사과가 있을 때
    elif q == 2:
        pass
    else:
        break
    cnt += 1

print(cnt+1)