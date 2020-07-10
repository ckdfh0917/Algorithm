N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
    q = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        if arr[x][i] == 1:
            q.append(i)
            visited[x][i] = 1

    while q:
        next = q.pop()
        if next == y:
            return True
        else:
            for i in range(N):
                if arr[next][i] == 1 and visited[next][i] == 0:
                    q.append(i)
                    visited[next][i] = 1
    return False

res = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if bfs(i, j):
            res[i][j] = 1

for i in range(N):
    print(' '.join(map(str, res[i])))