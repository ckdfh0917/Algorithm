import heapq
N, M = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     print(land[i])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 섬을 숫자로 다시 표기
def marking(x, y ,cnt):
    visited[x][y] = 1
    land[x][y] = cnt
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:
            if land[x+dx[i]][y+dy[i]] == 1 and visited[x+dx[i]][y+dy[i]] == 0:
                marking(x+dx[i], y+dy[i], cnt)
    return

# 가로 길이를 카운트
def row_cnt():
    for i in range(N):
        d = 0
        temp = 0
        for j in range(M):
            if temp == 0 and land[i][j] == 0:
                continue
            elif temp == 0 and land[i][j] != 0:
                temp = land[i][j]
            elif temp != 0 and land[i][j] == 0:
                d += 1
            elif land[i][j] != temp:
                heapq.heappush(pq, (d, land[i][j], temp))
                temp = land[i][j]
                d = 0
            elif land[i][j] == temp:
                d = 0
                continue

# 세로 길이를 카운트
def col_cnt():
    for j in range(M):
        d = 0
        temp = 0
        for i in range(N):
            if temp == 0 and land[i][j] == 0:
                continue
            elif temp == 0 and land[i][j] != 0:
                temp = land[i][j]
            elif temp != 0 and land[i][j] == 0:
                d += 1
            elif land[i][j] != temp:
                heapq.heappush(pq, (d, land[i][j], temp))
                temp = land[i][j]
                d = 0
            elif land[i][j] == temp:
                d = 0
                continue

# 유니온-파인드
def make_set(x):
    pi[x] = x

def find_set(x):
    if pi[x] == x:
        return x
    else:
        pi[x] = find_set(pi[x])
        return pi[x]

def union(x, y):
    py = pi[find_set(y)]
    px = pi[find_set(x)]
    pi[py] = px

cnt = 0
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if land[i][j] == 1:
            if visited[i][j] == 0:
                cnt += 1
                marking(i, j, cnt)

pq = []

col_cnt()
row_cnt()

pi = [0] * (cnt+1)

for i in range(1, cnt):
    make_set(i)

n = 0
ans = 0
while n < cnt-1:
    if not pq:
        ans = -1
        break
    d, a, b = heapq.heappop(pq)
    if d < 2:
        continue

    if find_set(a) == find_set(b):
        continue
    else:
        union(a, b)
        ans += d
        n += 1

print(ans)