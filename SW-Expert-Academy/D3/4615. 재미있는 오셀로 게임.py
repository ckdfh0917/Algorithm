import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
# 왼쪽 위부터 시계 방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def start(N):
    arr = [[0 for _ in range(N)] for _ in range(N)]
    temp = (N // 2) - 1
    arr[temp][temp] = 2
    arr[temp+1][temp+1] = 2
    arr[temp+1][temp] = 1
    arr[temp][temp+1] = 1

    return arr

def find(X,Y,k,arr):

    # 8개의 방향에 자신과 다른 돌이 놓여있는가
    nextX = 0
    nextY = 0
    a = []
    for i in range(8):
        nextX = X + dx[i]
        nextY = Y + dy[i]
        if nextX < len(arr) and nextY < len(arr) and nextX >= 0 and nextY >= 0:
            if arr[nextX][nextY] != k and arr[nextX][nextY] != 0:
                a.append(i)
    return a

def change(X,Y,k,arr,find_doll):
    for i in range(len(find_doll)):
        A = nextX =  X #+ dx[find_doll[i]]
        B = nextY =  Y #+ dy[find_doll[i]]
        tempX = 0
        tempY = 0
        cnt = 0
        #print('r', find_doll[i])
        while 1:
            nextX += dx[find_doll[i]]
            nextY += dy[find_doll[i]]
            if 0 <= nextX < N and 0 <= nextY < N:
                if arr[nextX][nextY] == 0:
                    cnt = 0
                    break
                elif arr[nextX][nextY] != k:
                    if 0 <= nextX + dx[find_doll[i]] < N and 0 <= nextY + dy[find_doll[i]] < N:
                        cnt += 1
                        if arr[nextX + dx[find_doll[i]]][nextY + dy[find_doll[i]]] == k:
                            tempX = nextX + dx[find_doll[i]]
                            tempY = nextY + dy[find_doll[i]]

                            #print('w',tempX,tempY, cnt)
                            break
                elif arr[nextX][nextY] == 0:
                    break
            else:
                cnt = 0
                break
        #print('t', tempX,tempY, cnt)

        for h in range(1,cnt+1):
            #print('x',X + h*dx[find_doll[i]], Y + h*dy[find_doll[i]])
            arr[X + h*dx[find_doll[i]]][Y + h*dy[find_doll[i]]] = k

    return arr


#흑돌 - 1
#백돌 - 2
for test_case in range(1,q+1):
    N, M = map(int, input().split())

    arr = start(N)
    #print(arr)

    for p in range(M):
        #print('--------{}-------'.format(p+1))
        x, y, k = map(int, input().split())     # (x,y)에 k돌 놓기

        X = x-1
        Y = y-1
        arr[X][Y] = k
        find_doll = find(X,Y,k,arr)
        #print(find_doll)
        cha = change(X,Y,k,arr,find_doll)

        # for i in range(N):
        #     print(cha[i])




    cntB = 0
    cntW = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cntB += 1
            elif arr[i][j] == 2:
                cntW += 1
    print('#{} {} {}' .format(test_case,cntB,cntW))