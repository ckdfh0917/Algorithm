import copy


N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

def up(arr):
    # 밀기
    for j in range(N):
        i = 0
        while i < N-1:
            if arr[i][j] == 0 and arr[i+1][j] != 0:
                k = i
                while k >= 0:
                    if arr[k][j] == 0 and arr[k + 1][j] != 0:
                        arr[k][j] = arr[k + 1][j]
                        arr[k + 1][j] = 0
                        k -= 1
                    else:
                        break
            else:
                i += 1
    # 합치기
    for j in range(N):
        i = 0
        while i < N-1:
            if arr[i][j] == arr[i+1][j]:
                arr[i][j] += arr[i+1][j]
                arr[i+1][j] = 0
                i += 2
            else:
                i += 1
    # 밀기
    for j in range(N):
        i = 0
        while i < N-1:
            if arr[i][j] == 0 and arr[i+1][j] != 0:
                k = i
                while k >= 0:
                    if arr[k][j] == 0 and arr[k + 1][j] != 0:
                        arr[k][j] = arr[k + 1][j]
                        arr[k + 1][j] = 0
                        k -= 1
                    else:
                        break
            else:
                i += 1
def down(arr):
    # 밀기
    for j in range(N):
        i = N-1
        while i > 0:
            if arr[i][j] == 0 and arr[i-1][j] != 0:
                k = i
                while k < N:
                    if arr[k][j] == 0 and arr[k - 1][j] != 0:
                        arr[k][j] = arr[k-1][j]
                        arr[k-1][j] = 0
                        k += 1
                    else:
                        break
            else:
                i -= 1
    # 합치기
    for j in range(N):
        i = N-1
        while i > 0:
            if arr[i][j] == arr[i-1][j]:
                arr[i][j] += arr[i-1][j]
                arr[i-1][j] = 0
                i -= 2
            else:
                i -= 1
    # 밀기
    for j in range(N):
        i = N-1
        while i > 0:
            if arr[i][j] == 0 and arr[i-1][j] != 0:
                k = i
                while k < N:
                    if arr[k][j] == 0 and arr[k - 1][j] != 0:
                        arr[k][j] = arr[k-1][j]
                        arr[k-1][j] = 0
                        k += 1
                    else:
                        break
            else:
                i -= 1
def right(arr):
    # 밀기
    for i in range(N):
        j = N-1
        while j > 0:
            if arr[i][j] == 0 and arr[i][j-1] != 0:
                k = j
                while k < N:
                    if arr[i][k] == 0 and arr[i][k-1] != 0:
                        arr[i][k] = arr[i][k-1]
                        arr[i][k-1] = 0
                        k += 1
                    else:
                        break
            else:
                j -= 1
    # 합치기
    for i in range(N):
        j = N-1
        while j > 0:
            if arr[i][j] == arr[i][j-1]:
                arr[i][j] += arr[i][j-1]
                arr[i][j-1] = 0
                j -= 2
            else:
                j -= 1
    # 밀기
    for i in range(N):
        j = N-1
        while j > 0:
            if arr[i][j] == 0 and arr[i][j-1] != 0:
                k = j
                while k < N:
                    if arr[i][k] == 0 and arr[i][k-1] != 0:
                        arr[i][k] = arr[i][k-1]
                        arr[i][k-1] = 0
                        k += 1
                    else:
                        break
            else:
                j -= 1
def left(arr):
    # 밀기
    for i in range(N):
        j = 0
        while j < N-1:
            if arr[i][j] == 0 and arr[i][j+1] != 0:
                k = j
                while k >= 0:
                    if arr[i][k] == 0 and arr[i][k+1] != 0:
                        arr[i][k] = arr[i][k+1]
                        arr[i][k+1] = 0
                        k -= 1
                    else:
                        break
            else:
                j += 1
    # 합치기
    for i in range(N):
        j = 0
        while j < N-1:
            if arr[i][j] == arr[i][j+1]:
                arr[i][j] += arr[i][j+1]
                arr[i][j+1] = 0
                j += 2
            else:
                j += 1
    # 밀기
    for i in range(N):
        j = 0
        while j < N-1:
            if arr[i][j] == 0 and arr[i][j+1] != 0:
                k = j
                while k >= 0:
                    if arr[i][k] == 0 and arr[i][k+1] != 0:
                        arr[i][k] = arr[i][k+1]
                        arr[i][k+1] = 0
                        k -= 1
                    else:
                        break
            else:
                j += 1

def command(x, a):
    if x == 0:
        up(a)
    elif x == 1:
        down(a)
    elif x == 2:
        right(a)
    elif x == 3:
        left(a)

res = 0

def dfs(index, board, cnt):
    global res

    command(index, board)

    if cnt == 5:
        t = 0
        for z in range(N):
            q = max(board[z])
            t = max(t, q)
        res = max(res, t)
        return

    for i in range(4):
        b = copy.deepcopy(board)
        dfs(i, b, cnt+1)

for i in range(4):
    newboard = copy.deepcopy(lst)
    dfs(i, newboard, 1)





print(res)