import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

dx = [-1,0,1,0] # 위 오른 아래 왼
dy = [0,1,0,-1]

for test_case in range(1,q+1):
    M, N, K = map(int, input().split())

    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    stack = []
    top = -1
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 1을 만나는 i,j를 x, y로
            if arr[i][j] == 1:
                x = i
                y = j
                cnt += 1
                tt = 0
                while True:
                    tt += 1
                    arr[x][y] = 0   # 방문 표시
                    for k in range(4):  # 사방 탐색
                        if 0 <= x+dx[k] < N and 0 <= y+dy[k] < M:   # 인덱스 조절
                            if arr[x+dx[k]][y+dy[k]] == 1:  # 사방 탐색에서 1을 찾으면
                                stack.append(x+dx[k])
                                stack.append(y+dy[k])
                                top += 1
                    # 이동하기
                    if top == -1:
                        break
                    else:
                        y = stack.pop()
                        x = stack.pop()
                        top -= 1

    print('{}' .format(cnt))

