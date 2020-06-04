arr = [list(map(int, input().split())) for _ in range(10)]

def check(x, y):
    checked = [0] * 6

    # 5 x 5 체크
    if paper[5] > 0 and 0 <= x+5 <= 10 and 0 <= y+5 <= 10:
        for k in range(5):
            if 0 in arr[x + k][y:y + 5]:
                checked[5] = 0
                break
            else:
                checked[5] = 1
    # 4 x 4 체크
    if paper[4] > 0 and 0 <= x+4 <= 10 and 0 <= y+4 <= 10:
        for k in range(4):
            if 0 in arr[x + k][y:y+4]:
                checked[4] = 0
                break
            else:
                checked[4] = 1
    # 3 x 3 체크
    if paper[3] > 0 and 0 <= x+3 <= 10 and 0 <= y+3 <= 10:
        for k in range(3):
            if 0 in arr[x + k][y:y + 3]:
                checked[3] = 0
                break
            else:
                checked[3] = 1
    # 2 x 2 체크
    if paper[2] > 0 and 0 <= x+2 <= 10 and 0 <= y+2 <= 10:
        for k in range(2):
            if 0 in arr[x + k][y:y + 2]:
                checked[2] = 0
                break
            else:
                checked[2] = 1
    # 1 x 1 체크
    if paper[1] > 0 and arr[x][y] == 1:
        checked[1] = 1

    return checked


def pull(x, y, k):
    if arr[x][y] == 1:
        flag = 0
    else:
        flag = 1
    for i in range(k):
        for j in range(k):
            arr[x+i][y+j] = flag

def dfs(cnt):
    global minV
    flag = False
    for i in range(10):
        if 1 in arr[i]:
            flag = True
            break

    if not flag:
        minV = min(minV, cnt)
        return
    elif cnt >= minV:
        return
    else:
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 1:
                    checked = check(i, j)
                    for k in range(5, 0, -1):
                        if checked[k] == 1:
                            checked[k] = 0
                            pull(i, j, k)
                            paper[k] -= 1
                            dfs(cnt+1)
                            paper[k] += 1
                            pull(i, j, k)
                            if checked.count(1) == 0:
                                return

paper = [0, 5, 5, 5, 5, 5]
minV = 1234567891

dfs(0)

if minV == 1234567891:
    minV = -1
print(minV)