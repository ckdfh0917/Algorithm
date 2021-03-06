n = int(input())

def command(c):

    if c == 'R+':
        temp1 = cube[0][0][2]
        temp2 = cube[0][1][2]
        temp3 = cube[0][2][2]

        cube[0][0][2] = cube[1][0][2]
        cube[0][1][2] = cube[1][1][2]
        cube[0][2][2] = cube[1][2][2]

        cube[1][0][2] = cube[5][0][2]
        cube[1][1][2] = cube[5][1][2]
        cube[1][2][2] = cube[5][2][2]

        cube[5][0][2] = cube[4][0][2]
        cube[5][1][2] = cube[4][1][2]
        cube[5][2][2] = cube[4][2][2]

        cube[4][0][2] = temp1
        cube[4][1][2] = temp2
        cube[4][2][2] = temp3

        # 시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[2][i][j]

        cube[2] = temp
    elif c == 'R-':
        temp1 = cube[0][0][2]
        temp2 = cube[0][1][2]
        temp3 = cube[0][2][2]

        cube[0][0][2] = cube[4][0][2]
        cube[0][1][2] = cube[4][1][2]
        cube[0][2][2] = cube[4][2][2]

        cube[4][0][2] = cube[5][0][2]
        cube[4][1][2] = cube[5][1][2]
        cube[4][2][2] = cube[5][2][2]

        cube[5][0][2] = cube[1][0][2]
        cube[5][1][2] = cube[1][1][2]
        cube[5][2][2] = cube[1][2][2]

        cube[1][0][2] = temp1
        cube[1][1][2] = temp2
        cube[1][2][2] = temp3

        # 반시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[2][i][j]

        cube[2] = temp
    elif c == 'L+':
        temp1 = cube[0][0][0]
        temp2 = cube[0][1][0]
        temp3 = cube[0][2][0]

        cube[0][0][0] = cube[4][0][0]
        cube[0][1][0] = cube[4][1][0]
        cube[0][2][0] = cube[4][2][0]

        cube[4][0][0] = cube[5][0][0]
        cube[4][1][0] = cube[5][1][0]
        cube[4][2][0] = cube[5][2][0]

        cube[5][0][0] = cube[1][0][0]
        cube[5][1][0] = cube[1][1][0]
        cube[5][2][0] = cube[1][2][0]

        cube[1][0][0] = temp1
        cube[1][1][0] = temp2
        cube[1][2][0] = temp3

        # 시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[3][i][j]

        cube[3] = temp

    elif c == 'L-':
        temp1 = cube[0][0][0]
        temp2 = cube[0][1][0]
        temp3 = cube[0][2][0]

        cube[0][0][0] = cube[1][0][0]
        cube[0][1][0] = cube[1][1][0]
        cube[0][2][0] = cube[1][2][0]

        cube[1][0][0] = cube[5][0][0]
        cube[1][1][0] = cube[5][1][0]
        cube[1][2][0] = cube[5][2][0]

        cube[5][0][0] = cube[4][0][0]
        cube[5][1][0] = cube[4][1][0]
        cube[5][2][0] = cube[4][2][0]

        cube[4][0][0] = temp1
        cube[4][1][0] = temp2
        cube[4][2][0] = temp3

        # 반시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[3][i][j]

        cube[3] = temp

    elif c == 'U+':
        temp1 = cube[4][2][0]
        temp2 = cube[4][2][1]
        temp3 = cube[4][2][2]

        cube[4][2][0] = cube[3][2][2]
        cube[4][2][1] = cube[3][1][2]
        cube[4][2][2] = cube[3][0][2]

        cube[3][2][2] = cube[1][0][2]
        cube[3][1][2] = cube[1][0][1]
        cube[3][0][2] = cube[1][0][0]

        cube[1][0][2] = cube[2][0][0]
        cube[1][0][1] = cube[2][1][0]
        cube[1][0][0] = cube[2][2][0]

        cube[2][0][0] = temp1
        cube[2][1][0] = temp2
        cube[2][2][0] = temp3

        # 시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[0][i][j]

        cube[0] = temp


    elif c == 'U-':
        temp1 = cube[4][2][0]
        temp2 = cube[4][2][1]
        temp3 = cube[4][2][2]

        cube[4][2][0] = cube[2][0][0]
        cube[4][2][1] = cube[2][1][0]
        cube[4][2][2] = cube[2][2][0]

        cube[2][0][0] = cube[1][0][2]
        cube[2][1][0] = cube[1][0][1]
        cube[2][2][0] = cube[1][0][0]

        cube[1][0][2] = cube[3][2][2]
        cube[1][0][1] = cube[3][1][2]
        cube[1][0][0] = cube[3][0][2]

        cube[3][2][2] = temp1
        cube[3][1][2] = temp2
        cube[3][0][2] = temp3

        # 반시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[0][i][j]

        cube[0] = temp
    elif c == 'D+':
        temp1 = cube[4][0][0]
        temp2 = cube[4][0][1]
        temp3 = cube[4][0][2]

        cube[4][0][0] = cube[2][0][2]
        cube[4][0][1] = cube[2][1][2]
        cube[4][0][2] = cube[2][2][2]

        cube[2][0][2] = cube[1][2][2]
        cube[2][1][2] = cube[1][2][1]
        cube[2][2][2] = cube[1][2][0]

        cube[1][2][2] = cube[3][2][0]
        cube[1][2][1] = cube[3][1][0]
        cube[1][2][0] = cube[3][0][0]

        cube[3][2][0] = temp1
        cube[3][1][0] = temp2
        cube[3][0][0] = temp3
        # 시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[5][i][j]

        cube[5] = temp

    elif c == 'D-':
        temp1 = cube[4][0][0]
        temp2 = cube[4][0][1]
        temp3 = cube[4][0][2]

        cube[4][0][2] = cube[3][0][0]
        cube[4][0][1] = cube[3][1][0]
        cube[4][0][0] = cube[3][2][0]

        cube[3][0][0] = cube[1][2][0]
        cube[3][1][0] = cube[1][2][1]
        cube[3][2][0] = cube[1][2][2]

        cube[1][2][0] = cube[2][2][2]
        cube[1][2][1] = cube[2][1][2]
        cube[1][2][2] = cube[2][0][2]

        cube[2][2][2] = temp3
        cube[2][1][2] = temp2
        cube[2][0][2] = temp1
        # 반시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[5][i][j]

        cube[5] = temp
    elif c == 'F+':
        temp1 = cube[0][2][0]
        temp2 = cube[0][2][1]
        temp3 = cube[0][2][2]

        cube[0][2][0] = cube[3][2][0]
        cube[0][2][1] = cube[3][2][1]
        cube[0][2][2] = cube[3][2][2]

        cube[3][2][0] = cube[5][0][2]
        cube[3][2][1] = cube[5][0][1]
        cube[3][2][2] = cube[5][0][0]

        cube[5][0][2] = cube[2][2][0]
        cube[5][0][1] = cube[2][2][1]
        cube[5][0][0] = cube[2][2][2]

        cube[2][2][0] = temp1
        cube[2][2][1] = temp2
        cube[2][2][2] = temp3

        # 시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[1][i][j]

        cube[1] = temp
    elif c == 'F-':
        temp1 = cube[0][2][0]
        temp2 = cube[0][2][1]
        temp3 = cube[0][2][2]

        cube[0][2][0] = cube[2][2][0]
        cube[0][2][1] = cube[2][2][1]
        cube[0][2][2] = cube[2][2][2]

        cube[2][2][0] = cube[5][0][2]
        cube[2][2][1] = cube[5][0][1]
        cube[2][2][2] = cube[5][0][0]

        cube[5][0][0] = cube[3][2][2]
        cube[5][0][1] = cube[3][2][1]
        cube[5][0][2] = cube[3][2][0]

        cube[3][2][2] = temp3
        cube[3][2][1] = temp2
        cube[3][2][0] = temp1

        # 반시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[1][i][j]

        cube[1] = temp
    elif c == 'B+':
        temp1 = cube[0][0][0]
        temp2 = cube[0][0][1]
        temp3 = cube[0][0][2]

        cube[0][0][0] = cube[2][0][0]
        cube[0][0][1] = cube[2][0][1]
        cube[0][0][2] = cube[2][0][2]

        cube[2][0][0] = cube[5][2][2]
        cube[2][0][1] = cube[5][2][1]
        cube[2][0][2] = cube[5][2][0]

        cube[5][2][2] = cube[3][0][0]
        cube[5][2][1] = cube[3][0][1]
        cube[5][2][0] = cube[3][0][2]

        cube[3][0][0] = temp1
        cube[3][0][1] = temp2
        cube[3][0][2] = temp3

        # 시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[4][i][j]

        cube[4] = temp
    elif c == 'B-':
        temp1 = cube[0][0][0]
        temp2 = cube[0][0][1]
        temp3 = cube[0][0][2]

        cube[0][0][0] = cube[3][0][0]
        cube[0][0][1] = cube[3][0][1]
        cube[0][0][2] = cube[3][0][2]

        cube[3][0][0] = cube[5][2][2]
        cube[3][0][1] = cube[5][2][1]
        cube[3][0][2] = cube[5][2][0]

        cube[5][2][2] = cube[2][0][0]
        cube[5][2][1] = cube[2][0][1]
        cube[5][2][0] = cube[2][0][2]

        cube[2][0][0] = temp1
        cube[2][0][1] = temp2
        cube[2][0][2] = temp3
        # 반시계 회전
        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[4][i][j]

        cube[4] = temp



    # print(c)
    # print('                   ', cube[4][0])
    # print('                   ', cube[4][1])
    # print('                   ', cube[4][2])
    # print()
    # print(cube[3][0], '   ', cube[0][0], '   ', cube[2][0])
    # print(cube[3][1], '   ', cube[0][1], '   ', cube[2][1])
    # print(cube[3][2], '   ', cube[0][2], '   ', cube[2][2])
    # print()
    # print('                   ', cube[1][0])
    # print('                   ', cube[1][1])
    # print('                   ', cube[1][2])
    # print()
    # print('                   ', cube[5][0])
    # print('                   ', cube[5][1])
    # print('                   ', cube[5][2])


for _ in range(n):
    num = int(input())
    arr = list(map(str, input().split()))
    # 초기 셋팅
    cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]]

    for i in range(len(arr)):
        command(arr[i])

    for i in range(3):
        print(''.join(cube[0][i]))
