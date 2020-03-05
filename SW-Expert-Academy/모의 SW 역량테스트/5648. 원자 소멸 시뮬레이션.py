q = int(input())

dx = [-1,0,1,0]     # 위 오른 아래 왼
dy = [0,1,0,-1]
# dir : 위 0 오른 1 아래 2 왼 3

def game(x, y, dx, dy):
    global cnt, i, j, flag
    # print(x,y)
    if x+dx == i and y+dy == j:
        # print('c',cnt)
        # print('======')
        return cnt

    # direction = -1    # 그냥 해준거
    if dx == -1 and dy == 0:    # 위
        direction = 0
    elif dx == 0 and dy == 1:   # 오른
        direction = 1
    elif dx == 1 and dy == 0:   # 아래
        direction = 2
    else: #if dx == 0 and dy == -1:  # 왼
        direction = 3

    if x+dx == -1:      # 윗벽을 부딪히면
        cnt += 1
        return
        game(x+dx,y+dy,1,0)   # 아래로
    elif x+dx == N:     # 아랫벽을 부딪히면
        cnt += 1
        return
        game(x+dx,y+dy,-1,0)  # 위로
    elif y+dy == -1:    # 왼쪽벽을 부딪히면
        cnt += 1
        return
        game(x+dx,y+dy,0,1)   # 오른쪽으로
    elif y+dy == N:     # 오른쪽벽을 부딪히면
        cnt += 1
        return
        game(x+dx,y+dy,0,-1)  # 왼쪽으로

    elif lst[x+dx][y+dy] == 0:
        game(x+dx,y+dy,dx,dy)
    elif lst[x+dx][y+dy] == 1:
        cnt += 1
        if direction == 0:          # 위로 부딪히면
            return
            game(x+dx,y+dy,1,0)     # 아래로
        elif direction == 1:        # 오른쪽으로 부딪히면
            return
            game(x+dx,y+dy,0,-1)    # 왼쪽으로
        elif direction == 2:        # 아래로 부딪히면
            game(x+dx,y+dy,0, 1)    # 오른쪽으로
        elif direction == 3:        # 왼쪽으로 부딪히면
            game(x+dx,y+dy,-1,0)    # 위로

    elif lst[x+dx][y+dy] == 2:
        cnt += 1
        if direction == 0:          # 위로 부딪히면
            game(x+dx,y+dy,0, 1)    # 오른쪽으로
        elif direction == 1:        # 오른쪽으로 부딪히면
            return
            game(x+dx,y+dy,0,-1)    # 왼쪽으로
        elif direction == 2:        # 아래로 부딪히면
            return
            game(x+dx,y+dy,-1,0)    # 위로
        elif direction == 3:        # 왼쪽으로 부딪히면
            game(x+dx,y+dy,1,0)     # 아래로

    elif lst[x+dx][y+dy] == 3:
        cnt += 1
        if direction == 0:          # 위로 부딪히면
            game(x+dx,y+dy,0,-1)    # 왼쪽으로
        elif direction == 1:        # 오른쪽으로 부딪히면
            game(x+dx,y+dy,1,0)     # 아래로
        elif direction == 2:        # 아래로 부딪히면
            return
            game(x+dx,y+dy,-1,0)    # 위로
        elif direction == 3:        # 왼쪽으로 부딪히면
            return
            game(x+dx,y+dy,0, 1)    # 오른쪽으로

    elif lst[x+dx][y+dy] == 4:
        cnt += 1
        if direction == 0:          # 위로 부딪히면)
            return
            game(x+dx,y+dy,1,0)     # 아래로
        elif direction == 1:        # 오른쪽으로 부딪히면
            game(x+dx,y+dy,-1,0)    # 위로
        elif direction == 2:        # 아래로 부딪히면
            game(x+dx,y+dy,0,-1)    # 왼쪽으로
        elif direction == 3:        # 왼쪽으로 부딪히면
            return
            game(x+dx,y+dy,0, 1)    # 오른쪽으로

    elif lst[x+dx][y+dy] == 5:
        cnt += 1
        if direction == 0:          # 위로 부딪히면
            return
            game(x+dx,y+dy,1,0)     # 아래로
        elif direction == 1:        # 오른쪽으로 부딪히면
            return
            game(x+dx,y+dy,0,-1)    # 왼쪽으로
        elif direction == 2:        # 아래로 부딪히면
            return
            game(x+dx,y+dy,-1,0)    # 위로
        elif direction == 3:        # 왼쪽으로 부딪히면
            return
            game(x+dx,y+dy,0, 1)    # 오른쪽으로

    elif lst[x+dx][y+dy] == 6:
        for m in range(N):
            for n in range(N):
                if m != x+dx and n != y+dy and lst[m][n] == 6:
                    game(m,n,dx,dy)
    elif lst[x+dx][y+dy] == 7:
        for m in range(N):
            for n in range(N):
                if m != x+dx and n != y+dy and lst[m][n] == 7:
                    game(m,n,dx,dy)
    elif lst[x+dx][y+dy] == 8:
        for m in range(N):
            for n in range(N):
                if m != x+dx and n != y+dy and lst[m][n] == 8:
                    game(m,n,dx,dy)
    elif lst[x+dx][y+dy] == 9:
        for m in range(N):
            for n in range(N):
                if m != x+dx and n != y+dy and lst[m][n] == 9:
                    game(m,n,dx,dy)
    elif lst[x+dx][y+dy] == 10:
        for m in range(N):
            for n in range(N):
                if m != x+dx and n != y+dy and lst[m][n] == 10:
                    game(m,n,dx,dy)
    elif lst[x+dx][y+dy] == -1:
        flag = 1
        return


for test_case in range(1,q+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))

    result = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                x = i
                y = j
                for k in range(4):
                    cnt = 0
                    flag = 0
                    # print('k', x,y)
                    game(x, y, dx[k], dy[k])
                    if flag == 0:
                        result = max(result, cnt*2-1)
                        # print('======',cnt*2+1,'=====')

                    else:
                        result = max(result, cnt)
                        # print('======',cnt,'=====')
    print('#{} {}'.format(test_case, result))
