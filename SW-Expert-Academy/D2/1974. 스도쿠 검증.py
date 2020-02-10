q = int(input())

for test_case in range(1, q + 1):
    doku = []

    for i in range(9):
        temp = list(map(int, input().split()))
        doku += [temp]

    # 전치행렬
    list_a = []
    for x in zip(*doku):
        list_a += [x]
    # print(list_a)

    result = 1

    # 가로
    for i in range(9):
        for k in range(1, 10):
            if doku[i].count(k) != 1:
                result = 0
                break
    # 세로
    for j in range(9):
        for k in range(1, 10):
            if list_a[j].count(k) != 1:
                result = 0
                break

    # 사각형
    # (1,1) (1,4) (1,7)
    # (4,1) (4,4) (4,7)
    # (7,1) (7,4) (7,7)
    list_b = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # print(j)
            temp = []
            for x in range(3):
                for y in range(3):
                    temp += [doku[x + i][y + j]]
            list_b += [temp]
    # print(list_b)

    for i in range(9):
        for k in range(1, 10):
            if list_b[i].count(k) != 1:
                result = 0
                break

    print('#{} {}'.format(test_case, result))









