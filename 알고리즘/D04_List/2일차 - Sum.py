for test_case in range(1, 11):
    q = int(input())

    # 입력 받을 리스트 초기화
    num_list = []

    # 입력 받음
    for i in range(100):
        num_list.append(list(map(int, input().split())))

    # 행, 열 리스트 초기화
    col_list = []
    row_list = []

    # 행들의 합 리스트
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += num_list[i][j]
        col_list.append(temp)

    # 열들의 합 리스트
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += num_list[j][i]
        row_list.append(temp)

    # 대각선1
    line1 = 0
    for i in range(100):
        line1 += num_list[i][i]
    # 대각선2
    line2 = 0
    for i in range(1, 101):
        line2 += num_list[100 - i][100 - i]

    row_max = max(row_list)
    col_max = max(col_list)

    # print(row_max, col_max, line1, line2)

    result = max(row_max, col_max, line1, line2)
    print('#{} {}'.format(test_case, result))