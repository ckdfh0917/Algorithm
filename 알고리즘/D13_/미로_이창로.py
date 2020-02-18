import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

dx = [-1,0,1,0]     # 위 오른 아래 왼
dy = [0,1,0,-1]

for test_case in range(1,q+1):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(input()))
    # 출발점 찾기
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                x, y = i, j
                break
        if x != 0:
            break

    stack = []
    result = 0
    while True:
        for k in range(4):
            if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                if arr[x+dx[k]][y+dy[k]] == '0':
                    stack.append(x+dx[k])
                    stack.append(y+dy[k])
                    arr[x + dx[k]][y + dy[k]] = '1'
                elif arr[x+dx[k]][y+dy[k]] == '3':
                    result = 1
                    break
        if result == 1:
            break
        if stack:
            y = stack.pop()
            x = stack.pop()
        else:
            result = 0
            break
    print('#{} {}'.format(test_case,result))

