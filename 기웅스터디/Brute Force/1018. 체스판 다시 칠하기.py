N, M = map(int, input().split())

chess = [input() for _ in range(N)]

# for i in range(N):
#     print(chess[i])

new_chess =[]


def fB(arr):
    flag = 'B'
    cnt = 0
    for i in range(8):
        # print('aaaaaaaaaaaaaaa')
        for j in range(8):
            if flag == 'B':
                # print(flag, arr[i][j])
                if arr[i][j] == 'W':
                    cnt += 1
                flag = 'W'
            elif flag == 'W':
                # print(flag, arr[i][j])
                if arr[i][j] == 'B':
                    cnt += 1
                flag = 'B'
        if flag == 'B':
            flag = 'W'
        elif flag == 'W':
            flag = 'B'
    #     print(cnt,'bbbbbbbbbbbbbb')
    # print('fb', cnt)
    return cnt

def fW(arr):
    flag = 'W'
    cnt = 0
    for i in range(8):
        for j in range(8):
            if flag == 'B':
                # print(flag, arr[i][j])
                if arr[i][j] == 'W':
                    cnt += 1
                flag = 'W'
            elif flag == 'W':
                # print(flag, arr[i][j])
                if arr[i][j] == 'B':
                    cnt += 1
                flag = 'B'
        if flag == 'B':
            flag = 'W'
        elif flag == 'W':
            flag = 'B'
    # print('fw', cnt)
    return cnt

minV = 12345678901
for i in range(0,N-8+1):
    for j in range(0,M-8+1):
        new_chess = []
        for k in range(8):
            new_chess.append(chess[i+k][j:j+8])

        minV = min(minV, fB(new_chess))
        minV = min(minV, fW(new_chess))
print(minV)



