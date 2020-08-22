N, M, H = map(int, input().split())

arr = [[0] * (N+2) for _ in range(H+2)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[a][b+1] = 2

for i in range(N+2):
    arr[H+1][i] = 3

for i in range(H+2):
    arr[i][0] = 3
    arr[i][N+1] = 3

def ladder():
    for i in range(1, N+2):
        col = i
        for row in range(1, H+2):
            if arr[row][col] == 1:
                col += 1
            elif arr[row][col] == 2:
                col -= 1
        if col != i:
            return False
    return True




def make_ladder(x, y, c):
    global ans
    if ans <= c:
        return

    lad = ladder()
    if lad:
        ans = min(ans, c)
        return

    if c == 3:
        return

    for i in range(x, H + 1):
        for j in range(y, N ):
            if arr[i][j] == 0 and arr[i][j + 1] == 0:
                arr[i][j] = 1
                arr[i][j+1] = 2

                make_ladder(i, j+1, c+1)
                arr[i][j] = 0
                arr[i][j+1] = 0
        y = 1


ans = 1234567890
make_ladder(1, 1, 0)

if ans == 1234567890:
    print(-1)
else:
    print(ans)
