q = int(input())

dxa = [-1,0,1,0]     # 위 오른 아래 왼
dya = [0,1,0,-1]
# dir : 위 0 오른 1 아래 2 왼 3

def game(x, y, dx, dy):
    global cnt, i, j, flag
    # print(x,y, cnt)
    while True:
        # print(x, y)
        if x+dx == i and y+dy == j:
            # print('c',cnt)
            # print('======')
            return

        # direction = -1    # 그냥 해준거
        if dx == -1 and dy == 0:    # 위
            direction = 0
        elif dx == 0 and dy == 1:   # 오른
            direction = 1
        elif dx == 1 and dy == 0:   # 아래
            direction = 2
        else:                       # if dx == 0 and dy == -1:  # 왼
            direction = 3

        if x+dx == -1:      # 윗벽을 부딪히면
            cnt += 1
            return
        elif x+dx == N:     # 아랫벽을 부딪히면
            cnt += 1
            return
        elif y+dy == -1:    # 왼쪽벽을 부딪히면
            cnt += 1
            return
        elif y+dy == N:     # 오른쪽벽을 부딪히면
            cnt += 1
            return
        elif lst[x+dx][y+dy] == 0:      # 진행 방향으로 계속 진행
            x += dx
            y += dy
            continue
        elif lst[x+dx][y+dy] == 1:
            cnt += 1
            if direction == 0:          # 위로 부딪히면
                return
            elif direction == 1:        # 오른쪽으로 부딪히면
                return
            elif direction == 2:        # 아래로 부딪히면 오른쪽
                x += dx
                y += dy
                dx = 0
                dy = 1
                continue
            elif direction == 3:        # 왼쪽으로 부딪히면 위로
                x += dx
                y += dy
                dx = -1
                dy = 0
                continue

        elif lst[x+dx][y+dy] == 2:
            cnt += 1
            if direction == 0:          # 위로 부딪히면
                x += dx
                y += dy
                dx = 0
                dy = 1
                continue
            elif direction == 1:        # 오른쪽으로 부딪히면
                return
            elif direction == 2:        # 아래로 부딪히면
                return
            elif direction == 3:        # 왼쪽으로 부딪히면 아래로
                x += dx
                y += dy
                dx = 1
                dy = 0
                continue

        elif lst[x+dx][y+dy] == 3:
            cnt += 1
            if direction == 0:          # 위로 부딪히면 왼쪽
                x += dx
                y += dy
                dx = 0
                dy = -1
                continue
            elif direction == 1:        # 오른쪽으로 부딪히면
                x += dx
                y += dy
                dx = 1
                dy = 0
                continue
            elif direction == 2:        # 아래로 부딪히면
                return
            elif direction == 3:        # 왼쪽으로 부딪히면
                return

        elif lst[x+dx][y+dy] == 4:
            cnt += 1
            if direction == 0:          # 위로 부딪히면)
                return
            elif direction == 1:        # 오른쪽으로 부딪히면
                x += dx
                y += dy
                dx = -1
                dy = 0
                continue
            elif direction == 2:        # 아래로 부딪히면
                x += dx
                y += dy
                dx = 0
                dy = -1
                continue
            elif direction == 3:        # 왼쪽으로 부딪히면
                return

        elif lst[x+dx][y+dy] == 5:
            cnt += 1
            if direction == 0:          # 위로 부딪히면
                return
            elif direction == 1:        # 오른쪽으로 부딪히면
                return
            elif direction == 2:        # 아래로 부딪히면
                return
            elif direction == 3:        # 왼쪽으로 부딪히면
                return

        elif lst[x+dx][y+dy] == 6:
            for m in range(N):
                f = 0
                for n in range(N):
                    if m != x+dx and n != y+dy and lst[m][n] == 6:
                        x = m
                        y = n
                        f = 1
                        break
                if f == 1:
                    break
        elif lst[x+dx][y+dy] == 7:
            for m in range(N):
                f = 0
                for n in range(N):
                    if m != x+dx and n != y+dy and lst[m][n] == 7:
                        x = m
                        y = n
                        f = 1
                        break
                if f == 1:
                    break
        elif lst[x+dx][y+dy] == 8:
            for m in range(N):
                f = 0
                for n in range(N):
                    if m != x+dx and n != y+dy and lst[m][n] == 8:
                        x = m
                        y = n
                        f = 1
                        break
                if f == 1:
                    break
        elif lst[x+dx][y+dy] == 9:
            for m in range(N):
                f = 0
                for n in range(N):
                    if m != x+dx and n != y+dy and lst[m][n] == 9:
                        x = m
                        y = n
                        f = 1
                        break
                if f == 1:
                    break
        elif lst[x+dx][y+dy] == 10:
            for m in range(N):
                f = 0
                for n in range(N):
                    if m != x+dx and n != y+dy and lst[m][n] == 10:
                        x = m
                        y = n
                        f = 1
                        break
                if f == 1:
                    break
        elif lst[x+dx][y+dy] == -1:
            flag = 1
            return
        else:
            return

for test_case in range(1, q+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    result = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                xa = i
                ya = j
                for k in range(4):
                    cnt = 0
                    flag = 0
                    # print('k', xa,ya)
                    game(xa, ya, dxa[k], dya[k])
                    if flag == 0:
                        result = max(result, cnt*2-1)
                        # print('======',cnt*2+1,'=====')

                    else:
                        result = max(result, cnt)
                        # print('======',cnt,'=====')
    print('#{} {}'.format(test_case, result))
