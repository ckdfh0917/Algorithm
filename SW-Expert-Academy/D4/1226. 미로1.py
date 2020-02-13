import sys
sys.stdin = open('input.txt', 'r')


dx = [-1,0,1,0] # 위 오른 아래 왼
dy = [0,1,0,-1]

for test_case in range(1,11):
    q = int(input())

# 현 위치에서 갈 수 있는 위치를 스택에 쌓고
# pop을 하면서 이동하고 방문표시함
# 이동을 하면서 3을 찾는다

    maze = []
    for _ in range(16):
        maze.append(list(map(int, input())))
    #print(maze)
    # 출발점 찾기
    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                x = i
                y = j
                break

    stack = []
    top = -1
    while True:

        flag = False
        # 사방 탐색
        for i in range(4):
            if 0 <= x+dx[i] < 100 and 0 <= y+dy[i] < 100:
                if maze[x+dx[i]][y+dy[i]] == 0:
                    stack.append(x+dx[i])
                    stack.append(y+dy[i])
                    top += 1
                elif maze[x+dx[i]][y+dy[i]] == 3:
                    result = 1
                    flag = True
                    break
                elif maze[x+dx[i]][y+dy[i]] != 0 and maze[x+dx[i]][y+dy[i]] != 1 and maze[x+dx[i]][y+dy[i]] != 3:
                    result = 0
                    flag = True
        if flag:
            break
        # 이동 전에 내가 방문했던 곳 표시
        maze[x][y] = 1

        # 이동
        if len(stack) != 0:
            y = stack.pop()
            x = stack.pop()
            top -= 1
        else:
            result =0
            break

    print('#{} {}'.format(test_case, result))