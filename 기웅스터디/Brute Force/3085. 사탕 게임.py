N = int(input())
sugar = [list(input()) for _ in range(N)]
# print(sugar)
# for i in range(N):
#     print(sugar[i])

dx = [-1,0,1,0]  # 위 오른 아래 왼
dy = [0,1,0,-1]

visited = [[0] * N for _ in range(N)]
maxV = 0
for i in range(N):
    for j in range(N):
        x, y = i, j
        for k in range(4):
            if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                tempX = x
                tempY = y
                sugar[x+dx[k]][y+dy[k]], sugar[x][y] = sugar[x][y], sugar[x+dx[k]][y+dy[k]]
                # print('==================')
                # print(x,y)
                # for a in range(N):
                #     print(sugar[a])
                cntX = 1
                cntY = 1
                if x+1 < N:
                    while sugar[x][y] == sugar[x+1][y]:
                        cntX += 1
                        x += 1
                        # print(x,y, end=' ')
                        if x+1 == N:
                            break
                x = tempX
                y = tempY
                if 0 <= x-1:
                    while sugar[x][y] == sugar[x-1][y]:
                        cntX += 1
                        x -= 1
                        # print(x,y, end=' ')
                        if x == 0:
                            break
                x = tempX
                y = tempY
                if y+1 < N:
                    while sugar[x][y] == sugar[x][y+1]:
                        cntY += 1
                        y += 1
                        # print(x,y, end=' ')
                        if y+1 == N:
                            break
                x = tempX
                y = tempY
                if 0 <= y-1:
                    while sugar[x][y] == sugar[x][y-1]:
                        cntY += 1
                        y -= 1
                        # print(x,y, end=' ')
                        if y == 0:
                            break

                x = tempX
                y = tempY
                maxV = max(maxV, cntY, cntX)
                # print()
                # print(maxV, cntX, cntY)
                sugar[x + dx[k]][y + dy[k]], sugar[x][y] = sugar[x][y], sugar[x + dx[k]][y + dy[k]]
print(maxV)