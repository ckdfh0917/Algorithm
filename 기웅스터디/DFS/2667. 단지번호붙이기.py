N = int(input())
apt = []
dx = [-1,0,1,0]  # 위 오른 아래 왼
dy = [0,1,0,-1]

for _ in range(N):
    apt.append(input())

visited = [[0] * N for _ in range(N)]
stack = []
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and apt[i][j] == '1':
            cnt += 1
            visited[i][j] = cnt
            stack.append([i, j])
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                        if apt[x+dx[k]][y+dy[k]] == '1' and visited[x+dx[k]][y+dy[k]] == 0:
                            stack.append([x+dx[k],y+dy[k]])
                            visited[x+dx[k]][y+dy[k]] = cnt
maxV = 0
for i in range(N):
    # print(visited[i])
    temp = max(visited[i])
    maxV = max(maxV, temp)
print(maxV)
res = [0] * (maxV+1)
for k in range(1, maxV+1):
    for i in range(N):
        for j in range(N):
            if k == visited[i][j]:
                res[k] += 1
res.sort()
for i in range(1,len(res)):
    print(res[i])
