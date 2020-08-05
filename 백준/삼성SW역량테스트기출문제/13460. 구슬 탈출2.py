from collections import deque
# https://juhee-maeng.tistory.com/29

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
minV = 123456891


p_r = [0, 0]
p_b = [0, 0]

for i in range(N):
    for j in range(M):
        if maze[i][j] == 'R':
            p_r = [i, j]
        if maze[i][j] == 'B':
            p_b = [i, j]

def move(x, y, dx, dy):
    move_cnt = 0
    while True:
        if maze[x+dx][y+dy] == '.':
            x += dx
            y += dy
        elif maze[x+dx][y+dy] == 'O':
            return x, y, -1
        else:
            return x, y, move_cnt

def bfs(p_r, p_b):
    rx, ry = p_r
    bx, by = p_b

    q = deque([[[[rx, ry, bx, by]], 0]])
    while q:
        visited, num = q.pop()
        rx = visited[-1][0]
        ry = visited[-1][1]
        bx = visited[-1][2]
        by = visited[-1][3]

        # 이동횟수가 10번을 넘긴다면 -1을 return한다.
        if num == 10:
            return -1

        for i in range(4):
            new_rx, new_ry, r_move = move(rx, ry, dx[i], dy[i])
            new_bx, new_by, b_move = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 탈출했다.
            if b_move == -1:
                pass
            # 파란 구슬은 탈출하지 못했고, 빨간 구슬은 탈출했다.
            elif r_move == -1:
                return num + 1
            # 파란 구슬도, 빨간 구슬도 탈출하지 못했다.
            else:
                if new_rx == new_bx and new_ry == new_by:  # 만약 서로 같은 공간에 있다면 move횟수로 위치를 조정해줘야한다.
                    if (r_move < b_move):  # 빨간 공이 덜 움직였다 -> 파란 공을 한칸 뒤로 물린다.
                        new_bx, new_by = new_bx - dx[i], new_by - dy[i]
                    else:  # 파란 공이 덜 움직였다. -> 빨간 공을 한칸 뒤로 물린다.
                        new_rx, new_ry = new_rx - dx[i], new_ry - dy[i]
                # [빨간공, 파란공] 해당 위치를 전에 방문한적이 없다면 큐에 append한다.
                if [new_rx, new_ry, new_bx, new_by] not in visited:
                    q.appendleft([visited + [[new_rx, new_ry, new_bx, new_by]], num + 1])
        # 4방향에 대해 알아봤으나 큐에 더이상 추가될 것이 없고,
        # 또한 현재 큐에는 남아있는 element가 없다.
        # -1을 return한다.
        if len(q) == 0:
            return -1

print(bfs(p_r, p_b))