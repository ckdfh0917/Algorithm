N, M, H = map(int, input().split())

arr = [[0] * (M+2) for _ in range(N+2)]
visited = [[0] * (M+2) for _ in range(N+2)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[a][b+1] = 2

for i in range(M+2):
    arr[N+1][i] = 3

for i in range(N+2):
    arr[i][0] = 3
    # print(arr[i])

def down(x, y, s):
    if arr[x][y] == 0:
        if down(x+1, y, s):
            return True
        else:
            return False
    elif arr[x][y] == 1:
        if down(x+1, y+1, s):
            return True
        else:
            return False
    elif arr[x][y] == 2:
        if down(x+1, y-1, s):
            return True
        else:
            return False
    else:
        if y == s:
            return True
        else:
            return False

def ladder():
    for i in range(1, M+2):
        f = down(0, i, i)
        # print('ff', i, f)
        if not f:
            return False
    return True



def make_ladder(c):
    global cnt
    print('ccc', c)
    if c > H:
        return
    if cnt < c:
        return

    lad = ladder()
    if lad:
        cnt = min(cnt, c)
        return

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] == 0 and arr[i][j + 1] == 0:
                if visited[i][j] == 0:
                    arr[i][j] = 1
                    arr[i][j+1] = 2
                    visited[i][j] = 1
                    print('aa', i, j)
                    make_ladder(c+1)
                    visited[i][j] = 0
                    arr[i][j] = 0
                    arr[i][j+1] = 0


cnt = 1234567890
if ladder():
    print(0)
else:
    make_ladder(0)
    print(cnt)
