import sys
sys.stdin = open('input.txt', 'r')

def xx(list):
    for i in range(100):
        for j in range(i,100):
            list[i][j],list[j][i] = list[j][i],list[i][j]
    return list

for test_case in range(1,11):
    q = int(input())
    print('#{} '.format(test_case), end='')
    arr= []
    for _ in range(100):
        arr.append(list(input()))
    max_col = 1
    for i in range(100):
        for j in range(100):
            col1,col2 = 0, 0
            for k in range(100):
                if 0 <= j-1-k < 100 and 0 <= j+1+k < 100:
                    # 양 옆이 같으면
                    if arr[i][j-1-k] == arr[i][j+1+k]:
                        col1 = 2*k+3
                        continue
                    elif arr[i][j-1-k] != arr[i][j+1+k]:
                        break
            if max_col < col1:
                max_col = col1
            for k in range(100):
                if 0 <= j - 1 - k < 100 and 0 <= j + 1 + k < 100:
                    # 오른쪽만 같다면
                    if arr[i][j - k] == arr[i][j + 1 + k]:
                        col2 = 2 * k + 2
                        continue
                    elif arr[i][j - k] != arr[i][j + 1 + k]:
                        break
                else:
                    break
            if max_col < col2:
                max_col = col2

    arr = xx(arr)
    max_row = 1
    for i in range(100):
        for j in range(100):
            row1, row2 = 0, 0
            for k in range(100):
                if 0 <= j - 1 - k < 100 and 0 <= j + 1 + k < 100:
                    # 양 옆이 같으면
                    if arr[i][j - 1 - k] == arr[i][j + 1 + k]:
                        row1 = 2 * k + 3
                        continue
                    elif arr[i][j - 1 - k] != arr[i][j + 1 + k]:
                        break
            if max_row < row1:
                max_row = row1
            for k in range(100):
                if 0 <= j - 1 - k < 100 and 0 <= j + 1 + k < 100:
                    # 오른쪽만 같다면
                    if arr[i][j - k] == arr[i][j + 1 + k]:
                        row2 = 2 * k + 2
                        continue
                    elif arr[i][j - k] != arr[i][j + 1 + k]:
                        break
                else:
                    break
            if max_row < row2:
                max_row = row2
    if max_col > max_row:
        result = max_col
    else:
        result = max_row
    print(result)
