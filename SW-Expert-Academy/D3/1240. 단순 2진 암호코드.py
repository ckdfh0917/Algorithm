q = int(input())

for test_case in range(1,q+1):
    n, m = map(int, input().split())  # 세로, 가로
    numbers = [list(map(int, input())) for _ in range(n)]
    print('#{} ' .format(test_case), end='')
    result = 0
    for i in range(n):
        for j in range(m-56+1):
            # print('a',i, j)
            code = []
            for p in range(j,j+56,7):
                temp = []
                cnt0 = 1
                cnt1 = 1
                for k in range(p, p+6):
                    if numbers[i][k] == 0 and numbers[i][k+1] == 0:
                        cnt0 += 1
                    elif numbers[i][k] == 0 and numbers[i][k+1] == 1:
                        temp.append(cnt0)
                        cnt0 = 1
                    elif numbers[i][k] == 1 and numbers[i][k+1] == 1:
                        cnt1 += 1
                    elif numbers[i][k] == 1 and numbers[i][k+1] == 0:
                        temp.append(cnt1)
                        cnt1 = 1
                if numbers[i][p+6] == 1:
                    temp.append(cnt1)
                # print('ttt',temp)
                if len(temp) == 4:
                    if temp[0] == 3 and temp[1] == 2 and temp[2] == 1 and temp[3] == 1:
                        code.append(0)
                    elif temp[0] == 2 and temp[1] == 2 and temp[2] == 2 and temp[3] == 1:
                        code.append(1)
                    elif temp[0] == 2 and temp[1] == 1 and temp[2] == 2 and temp[3] == 2:
                        code.append(2)
                    elif temp[0] == 1 and temp[1] == 4 and temp[2] == 1 and temp[3] == 1:
                        code.append(3)
                    elif temp[0] == 1 and temp[1] == 1 and temp[2] == 3 and temp[3] == 2:
                        code.append(4)
                    elif temp[0] == 1 and temp[1] == 2 and temp[2] == 3 and temp[3] == 1:
                        code.append(5)
                    elif temp[0] == 1 and temp[1] == 1 and temp[2] == 1 and temp[3] == 4:
                        code.append(6)
                    elif temp[0] == 1 and temp[1] == 3 and temp[2] == 1 and temp[3] == 2:
                        code.append(7)
                    elif temp[0] == 1 and temp[1] == 2 and temp[2] == 1 and temp[3] == 3:
                        code.append(8)
                    elif temp[0] == 3 and temp[1] == 1 and temp[2] == 1 and temp[3] == 2:
                        code.append(9)
                else:
                    continue
                if len(code) == 8:
                    # print('c1',code)
                    solve_sum = (code[0] + code[2] + code[4] + code[6]) * 3 + (code[1] + code[3] + code[5] + code[7])
                    solve_ten = solve_sum // 10
                    detect = (solve_ten + 1) * 10 - solve_sum
                    code.append(detect)
                    if detect == 10:
                        result = sum(code) - 10
                    else:
                        result = 0
                    # print('c2',code)
                    break
            if result != 0:
                break
        if result != 0:
            break
    print(result)