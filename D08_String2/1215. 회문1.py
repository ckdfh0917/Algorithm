import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1,11):
    num = int(input())
    print('#{} '.format(test_case), end='')
    arr= []
    for _ in range(8):
        arr.append(list(input()))
    #print(arr)

    col = 0
    # 가로 찾기
    for i in range(8):
        for j in range(9-num):
            flag1 = 0
            for k in range(num//2):
                if 0 <=j+num-1-k < 8 and 0 <= j+k < 8:
                    if arr[i][j+k] == arr[i][j+num-1-k]:
                        flag1 = 1
                        continue
                    elif arr[i][j+k] != arr[i][j+num-1-k]:
                        flag1 = 0
                        break
                else:
                    break
            if flag1 == 1:
                #print(i,arr[i][j:j+num])
                col += 1
    #print(col)
    row = 0
    # 세로 찾기
    for i in range(8):
        for j in range(8):
            flag2 = 0
            for k in range(num//2):
                if 0 <= j+num-1-k < 8 and 0 <= j+k < 8:
                    if arr[j+k][i] == arr[j+num-1-k][i]:
                        flag2 = 1
                        continue
                    elif arr[j+k][i] != arr[j+num-1-k][i]:
                        flag2 = 0
                        break
                else:
                    break
            if flag2 == 1:
                #print(j,i,arr[j][i],arr[j+1][i],arr[j+2][i],arr[j+3][i])
                row += 1
    #print(row)
    result = col + row

    print(result)

