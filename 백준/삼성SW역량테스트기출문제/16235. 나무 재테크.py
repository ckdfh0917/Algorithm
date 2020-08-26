N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]

tree = [[[] for _ in range(N)] for _ in range(N)]
energy = [[5] * (N) for _ in range(N)]

for i in range(M):
    x, y, z = info[i]
    tree[x-1][y-1].append(z)


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 여름에 추가되는 양분
plus = [[0] * N for _ in range(N)]

def spring():
    for i in range(N):
        for j in range(N):
            e = energy[i][j]
            idx = len(tree[i][j])
            flag = False
            for k in range(len(tree[i][j])):
                if e >= tree[i][j][k]:
                    energy[i][j] -= tree[i][j][k]
                    e -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    plus[i][j] += tree[i][j][k] // 2
                    if flag:
                        continue
                    flag = True
                    idx = k
            tree[i][j] = tree[i][j][0:idx]

def summer():
    for i in range(N):
        for j in range(N):
            if plus[i][j]:
                energy[i][j] += plus[i][j]
                plus[i][j] = 0
    return

def fall():
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                continue
            for k in range(len(tree[i][j])):
                t = tree[i][j][k] % 5
                if t == 0:
                    for p in range(8):
                        if 0 <= i+dx[p] < N and 0 <= j+dy[p] < N:
                            tree[i+dx[p]][j+dy[p]].insert(0, 1)

def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += A[i][j]

def season():
    for i in range(1, K+1):
        spring()
        summer()
        fall()
        winter()

season()

ans = 0
for i in range(N):
    # print(tree[i])
    for j in range(N):
        ans += len(tree[i][j])
print(ans)