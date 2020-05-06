# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
def transfer(hex):
    if hex == '0':
        return '0000'
    elif hex == '1':
        return '0001'
    elif hex == '2':
        return '0010'
    elif hex == '3':
        return '0011'
    elif hex == '4':
        return '0100'
    elif hex == '5':
        return '0101'
    elif hex == '6':
        return '0110'
    elif hex == '7':
        return '0111'
    elif hex == '8':
        return '1000'
    elif hex == '9':
        return '1001'
    elif hex == 'A':
        return '1010'
    elif hex == 'B':
        return '1011'
    elif hex == 'C':
        return '1100'
    elif hex == 'D':
        return '1101'
    elif hex == 'E':
        return '1110'
    elif hex == 'F':
        return '1111'

decoder = {112:0, 122:1, 221:2, 114:3, 231:4,132:5, 411:6, 213:7, 312:8, 211:9}


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]


    # 바코드 내에서 암호코드 찾기
    key_holder = []
    new_arr = [''] * N
    key = ''
    # HexToBin
    for i in range(N):
        for j in range(M):
            new_arr[i] += transfer(arr[i][j])

    # for i in range(N):
    #     for j in range(M*4-1):
    #         print(new_arr[i][j], end='')
    #     print()
    # 연속된 0 갯수, 1 갯수를 뒤에서 부터 찾기
    for i in range(N):
        # print(i)
        x1 = x2 = x3 = 0
        for j in range(M*4-1, -1, -1):
            if new_arr[i][j] == '1' and x2 == 0:
                x3 += 1
            elif new_arr[i][j] == '0' and x3 != 0 and x1 == 0:
                x2 += 1
            elif new_arr[i][j] == '1' and x2 != 0:
                x1 += 1
            elif new_arr[i][j] == '0' and x1 != 0:
                minV = min(x1, x2, x3)
                key = str(decoder[x3//minV*100 + x2//minV*10 + x1//minV]) + key
                x1 = x2 = x3 = 0
                # print('kk', len(key), key)
            if len(key) == 8:
                if key not in key_holder:
                    # print(key)
                    key_holder.append(key)
                key = ''
    # print(key_holder)
    answer = 0
    # 찾아낸 암호코드에서 코드 추출
    for x in key_holder:
        k = 0
        d = ''
        # print(x)
        define = (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) * 3 + (int(x[1]) + int(x[3]) + int(x[5])) + int(x[7])
        # print(define)
        if define % 10 == 0:
            temp = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7])
            answer += temp
        # print('ppp',answer)

    print('#{} {}'.format(test_case, answer))








