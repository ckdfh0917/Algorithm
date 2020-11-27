import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

arr = [[0] * C for _ in range(R)]
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark = [r, c, s, d, z]
    sharks.append(shark)
    arr[r-1][c-1] = [s, d, z]


def move_shark():
    global arr
    narr = [[0] * C for _ in range(R)]
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0:
                a, b = i, j
                s, d, z = arr[i][j]
                if d < 3:
                    ns = s % (R*2 -2)
                else:
                    ns = s % (C*2 - 2)
                temp[a][b] = 1

                for k in range(ns):
                    temp[a][b] = 0
                    if d == 1:          # 위
                        if 0 <= a-1:    # 맨위가 아니라면
                            a -= 1
                            temp[a][b] = 1
                        else:           # 맨 위라면
                            a += 1
                            temp[a][b] = 1
                            d = 2
                    elif d == 2:        # 아래
                        if a+1 < R:     # 맨 아래가 아니라면
                            a += 1
                            temp[a][b] = 1
                        else:           # 맨 아래라면
                            a -= 1
                            temp[a][b] = 1
                            d = 1
                    elif d == 3:        # 오른쪽
                        if b+1 < C:     # 맨 오른쪽이 아니라면
                            b += 1
                            temp[a][b] = 1
                        else:           # 맨 오른쪽이라면
                            b -= 1
                            temp[a][b] = 1
                            d = 4
                    else:               # 왼쪽
                        if 0 <= b-1:    # 맨 왼쪽이 아니라면
                            b -= 1
                            temp[a][b] = 1
                        else:           # 맨 왼쪽이라면
                            b += 1
                            temp[a][b] = 1
                            d = 3

                    # for q in range(R):
                    #     print(temp[q])
                    # print()
                temp[a][b] = 0
                if narr[a][b] == 0:
                    narr[a][b] = [s, d, z]
                elif narr[a][b][2] < z:
                    narr[a][b] = [s, d, z]
                # for p in range(R):
                #     print(narr[p])
    arr = [narr[i][:] for i in range(R)]
cnt = 0
# 1. 낚시왕이 오른쪽으로 한 칸 이동
for j in range(C):
    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for i in range(R):
        if arr[i][j] != 0:
            cnt += arr[i][j][2]
            arr[i][j] = 0
            break
    # 3. 상어가 이동한다.
    move_shark()
print(cnt)