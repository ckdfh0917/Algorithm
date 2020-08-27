import sys
sys.setrecursionlimit(100000)
# 재귀 제한을 풀어야함
# 안그러면 런타임 에러
# 틀린게 없는거 같은데 자꾸 런타임 에러가 발생해서 시간 소요가 발생함

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * (M+1) for _ in range(N+1)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, cnt, flag):
    global ans
    if cnt >= ans:
        return

    if x == N-1 and y == M-1:
        ans = min(ans, cnt)
        if ans == N + M - 1:
            print(ans)
            exit(0)
        return

    for k in range(4):
        if 0 <= x+dx[k] < N and 0 <= y+dy[k] < M:
            if arr[x+dx[k]][y+dy[k]] == 0:
                if visited[x+dx[k]][y+dy[k]] == 0:
                    visited[x+dx[k]][y+dy[k]] = 1
                    dfs(x+dx[k], y+dy[k], cnt+1, flag)
                    visited[x+dx[k]][y+dy[k]] = 0
            elif not flag:
                if visited[x+dx[k]][y+dy[k]] == 0:
                    visited[x+dx[k]][y+dy[k]] = 1
                    dfs(x+dx[k], y+dy[k], cnt+1, 1)
                    visited[x+dx[k]][y+dy[k]] = 0
    return


ans = 1234567890
visited[0][0] = 1
dfs(0, 0, 1, 0)


if ans == 1234567890:
    ans = -1
print(ans)
