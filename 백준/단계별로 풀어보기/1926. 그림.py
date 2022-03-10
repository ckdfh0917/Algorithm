from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

q = deque()
res = 0
# bfs
def bfs():
    global res
    cnt = 1
    while q:
        x, y = q.popleft()
        #print(x, y, cnt, res)

        for k in range(4):
            if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m:
                # print("pp", x+dx[k], y+dy[k])
                if visited[x+dx[k]][y+dy[k]] == 0:
                    if arr[x+dx[k]][y+dy[k]] == 1:
                        cnt += 1
                        visited[x+dx[k]][y+dy[k]] = 1
                        q.append([x+dx[k], y+dy[k]])
    res = max(res, cnt)

pic_cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and arr[i][j] == 1:
            pic_cnt += 1
            #print("=====================", i, j)
            q.append([i, j])
            visited[i][j] = 1
            bfs()
            #print(res)
print(pic_cnt)
print(res)