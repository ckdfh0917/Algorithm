T = int(input())

for test_case in range(1, T+1):
    H, W = map(int, input().split())

    field = [list(input()) for _ in range(H)]
    k = int(input())
    cmd = input()

    # for i in range(H):
    #     print(field[i])
    # print('=====================')
    for x in range(k):
        if cmd[x] == 'S':
            flag = 0
            a, b = 0, 0
            for i in range(H):
                for j in range(W):
                    if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                        a, b = i, j
                        flag = 1
                        break
                if flag == 1:
                    break
            if field[a][b] == '^':
                for i in range(H):
                    if a-i >= 0:
                        if field[a-i][b] == '*':
                            field[a-i][b] = '.'
                            break
                        elif field[a-i][b] == '#':
                            break
                    else:
                        break
            elif field[a][b] == 'v':
                for i in range(H):
                    if a+i < H:
                        if field[a+i][b] == '*':
                            field[a+i][b] = '.'
                            break
                        elif field[a+i][b] == '#':
                            break
                    else:
                        break
            elif field[a][b] == '<':
                for i in range(W):
                    if b-i >= 0:
                        if field[a][b-i] == '*':
                            field[a][b-i] = '.'
                            break
                        elif field[a][b-i] == '#':
                            break
                    else:
                        break
            elif field[a][b] == '>':
                for i in range(W):
                    if b+i < W:
                        if field[a][b+i] == '*':
                            field[a][b+i] = '.'
                            break
                        elif field[a][b+i] == '#':
                            break
                    else:
                        break
        elif cmd[x] == 'U':
            flag = 0
            for i in range(H):
                for j in range(W):
                    if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                        if i-1 >= 0:
                            if field[i-1][j] == '.':
                                field[i-1][j] = '^'
                                field[i][j] = '.'
                            else:
                                field[i][j] = '^'
                        else:
                            field[i][j] = '^'
                        flag = 1
                        break
                if flag == 1:
                    break
        elif cmd[x] == 'D':
            flag = 0
            for i in range(H):
                for j in range(W):
                    if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                        if i+1 < H:
                            if field[i+1][j] == '.':
                                field[i+1][j] = 'v'
                                field[i][j] = '.'
                            else:
                                field[i][j] = 'v'
                        else:
                            field[i][j] = 'v'
                        flag = 1
                        break
                if flag == 1:
                    break
        elif cmd[x] == 'L':
            flag = 0
            for i in range(H):
                for j in range(W):
                    if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                        if j-1 >= 0:
                            if field[i][j-1] == '.':
                                field[i][j-1] = '<'
                                field[i][j] = '.'
                            else:
                                field[i][j] = '<'
                        else:
                            field[i][j] = '<'
                        flag = 1
                        break
                if flag == 1:
                    break
        elif cmd[x] == 'R':
            flag = 0
            for i in range(H):
                for j in range(W):
                    if field[i][j] == '^' or field[i][j] == 'v' or field[i][j] == '<' or field[i][j] == '>':
                        if j+1 < W:
                            if field[i][j+1] == '.':
                                field[i][j+1] = '>'
                                field[i][j] = '.'
                            else:
                                field[i][j] = '>'
                        else:
                            field[i][j] = '>'
                        flag = 1
                        break
                if flag == 1:
                    break
    print('#{} '.format(test_case), end='')
    for i in range(H):
        print(''.join(field[i]))