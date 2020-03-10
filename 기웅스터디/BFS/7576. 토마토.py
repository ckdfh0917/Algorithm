from collections import deque
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]

dx = [-1,0,1,0] # 위 오른 아래 왼
dy = [0,1,0,-1]

# print(box)
stack = []
empty = []
q = deque([])

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            stack.append([i, j])
            q.append([i, j])
        elif box[i][j] == -1:
            empty.append([i, j])
cnt = 0
while q:
    cnt += 1
    # print(cnt)
    # print(q)
    for _ in range(len(q)):
        #####################
        x, y = q.popleft()   # 원래는 이부분이 q.pop(0)로 하면 시간 초과가 뜨고
                             # q.popleft()로 하니까 통과됨
        ######################
        for k in range(4):
            if 0 <= x+dx[k] < M and 0 <= y+dy[k] < N and box[x+dx[k]][y+dy[k]] == 0:
                box[x+dx[k]][y+dy[k]] = 1
                q.append([x+dx[k], y+dy[k]])

    # for i in range(M):
    #     print(box[i])
flag = 0

for i in range(M):
    if box[i].count(0) != 0:
        flag = 1
        print(-1)
        break
else:
    print(cnt-1)