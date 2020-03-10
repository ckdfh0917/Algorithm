T = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]  # 1시2시4시5시7시8시10시11시
dy = [1,2,2,1,-1,-2,-2,-1]


for _ in range(T):
    I = int(input())

    chess = [[0] * I for _ in range(I)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    visited[x1][y1] = 1
    cnt = 0
    q = [[x1, y1]]

    while True:
        if visited[x2][y2] != 0:
            break
        cnt += 1
        for i in range(len(q)):
            x, y = q.pop(0)
            for k in range(8):
                if 0 <= x+dx[k] < I and 0 <= y+dy[k] < I:
                    if visited[x+dx[k]][y+dy[k]] == 0:
                        visited[x+dx[k]][y+dy[k]] = cnt
                        q.append([x+dx[k],y+dy[k]])
        # for i in range(I):
        #     print(visited[i])
        # print('========================')
    print(cnt)