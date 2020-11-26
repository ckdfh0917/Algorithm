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
    elif c == 'U+':
        temp1 = cube[4][0][0]
        temp2 = cube[4][0][1]
        temp3 = cube[4][0][2]
        temp4 = cube[4][1][0]
        temp5 = cube[4][1][1]
        temp6 = cube[4][1][2]


        cube[4][0][0] = cube[2][0][2]
        cube[4][0][1] = cube[2][1][2]
        cube[4][0][2] = cube[2][2][2]
        cube[4][1][0] = cube[2][0][1]
        cube[4][1][1] = cube[2][1][1]
        cube[4][1][2] = cube[2][2][1]

        cube[2][0][2] = cube[1][2][2]
        cube[2][1][2] = cube[1][2][1]
        cube[2][2][2] = cube[1][2][0]
        cube[2][0][1] = cube[1][1][2]
        cube[2][1][1] = cube[1][1][1]
        cube[2][2][1] = cube[1][1][0]

        cube[1][2][2] = cube[3][2][0]
        cube[1][2][1] = cube[3][1][0]
        cube[1][2][0] = cube[3][0][0]
        cube[1][1][2] = cube[3][2][1]
        cube[1][1][1] = cube[3][1][1]
        cube[1][1][0] = cube[3][0][1]

        cube[3][2][0] = temp1
        cube[3][1][0] = temp2
        cube[3][0][0] = temp3
        cube[3][2][1] = temp4
        cube[3][1][1] = temp5
        cube[3][0][1] = temp6


        temp = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2-i] = cube[5][i][j]

        cube[5] = temp
    elif c == 'U-':
        temp1 = cube[4][0][0]
        temp2 = cube[4][0][1]
        temp3 = cube[4][0][2]
        temp4 = cube[4][1][0]
        temp5 = cube[4][1][1]
        temp6 = cube[4][1][2]


        cube[4][0][0] = cube[3][2][0]
        cube[4][0][1] = cube[3][1][0]
        cube[4][0][2] = cube[3][0][0]
        cube[4][1][0] = cube[3][2][1]
        cube[4][1][1] = cube[3][1][1]
        cube[4][1][2] = cube[3][0][1]

        cube[3][2][0] = cube[1][2][2]
        cube[3][1][0] = cube[1][2][1]
        cube[3][0][0] = cube[1][2][0]
        cube[3][2][1] = cube[1][1][2]
        cube[3][1][1] = cube[1][1][1]
        cube[3][0][1] = cube[1][1][0]

        cube[1][2][2] = cube[2][0][2]
        cube[1][2][1] = cube[2][1][2]
        cube[1][2][0] = cube[2][2][2]
        cube[1][1][2] = cube[2][0][1]
        cube[1][1][1] = cube[2][1][1]
        cube[1][1][0] = cube[2][2][1]

        cube[2][0][2] = temp1
        cube[2][1][2] = temp2
        cube[2][2][2] = temp3
        cube[2][0][1] = temp4
        cube[2][1][1] = temp5
        cube[2][2][1] = temp6

        temp = [[0] * 3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                temp[2-j][i] = cube[5][i][j]

        cube[5] = temp

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

        cube[5][0][2] = cube[3][2][2]
        cube[5][0][1] = cube[3][2][1]
        cube[5][0][0] = cube[3][2][0]

        cube[3][2][2] = temp3
        cube[3][2][1] = temp2
        cube[3][2][0] = temp1
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




    print(c)
    print('                   ', cube[4][0])
    print('                   ', cube[4][1])
    print('                   ', cube[4][2])
    print()
    print(cube[3][0], '   ', cube[0][0], '   ', cube[2][0])
    print(cube[3][1], '   ', cube[0][1], '   ', cube[2][1])
    print(cube[3][2], '   ', cube[0][2], '   ', cube[2][2])
    print()
    print('                   ', cube[1][0])
    print('                   ', cube[1][1])
    print('                   ', cube[1][2])
    print()
    print('                   ', cube[5][0])
    print('                   ', cube[5][1])
    print('                   ', cube[5][2])


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
        print(cube[0][i])
    print()