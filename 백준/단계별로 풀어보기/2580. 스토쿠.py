# 스도쿠 규칙을 체크하는 것일 매번 하는 방법은 안됨

import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

col = [[0] * 10 for _ in range(9)]
row = [[0] * 10 for _ in range(9)]
square = [[0] * 10 for _ in range(9)]


def dfs(cnt):
    # print(cnt)
    if cnt == 81:
        for i in range(9):
            print(' '.join(map(str, arr[i])))
        exit(0)
        return

    x = cnt // 9
    y = cnt % 9
    # print(x, y, arr[x][y])
    if arr[x][y]:
        dfs(cnt+1)
    else:
        for k in range(1, 10):
            # print('k', k, col[y][k], row[x][k], square[square_idx(x, y)][k])
            if not col[y][k] and not row[x][k] and not square[square_idx(x, y)][k]:
                arr[x][y] = k
                col[y][k] = 1
                row[x][k] = 1
                square[square_idx(x, y)][k] = 1
                dfs(cnt+1)
                arr[x][y] = 0
                col[y][k] = 0
                row[x][k] = 0
                square[square_idx(x, y)][k] = 0


def square_idx(x, y):
    if 0 <= x < 3:
        if 0 <= y < 3:
            return 0
        elif 3 <= y < 6:
            return 1
        elif 6 <= y < 9:
            return 2
    elif 3 <= x < 6:
        if 0 <= y < 3:
            return 3
        elif 3 <= y < 6:
            return 4
        elif 6 <= y < 9:
            return 5
    elif 6 <= x < 9:
        if 0 <= y < 3:
            return 6
        elif 3 <= y < 6:
            return 7
        elif 6 <= y < 9:
            return 8

for i in range(9):
    for j in range(9):
        if arr[i][j]:
            col[j][arr[i][j]] = 1
            row[i][arr[i][j]] = 1
            square[square_idx(i, j)][arr[i][j]] = 1


dfs(0)

