from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])
        elif arr[i][j] == 1:
            home.append([i, j])
no_arr = [arr[i][:] for i in range(N)]

for i in range(len(chicken)):
    x, y = chicken[i]
    no_arr[x][y] = 0

# 1. M 개의 치킨집 선정 -> 순열(백트래킹)
# 2. 도시의 치킨거리 구하기
    # 2-1. 각 집과 선정된 치킨집 거리 중 가장 최소값 구하기
    # 2-2. 치킨 거리를 합하여 구한 도시의 치킨 거리 중 도시의 치킨거리가 가장 짧은 것을 구함

selected = []
def sel_chicken(index, cnt):
    if cnt == M:
        distance()

        return
    for i in range(index, len(chicken)):
        selected.append(chicken[i])
        sel_chicken(i+1, cnt+1)
        selected.pop()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 1234567890
def distance():
    dis = 0
    global res
    for i in range(len(home)):
        cnt = 13457890
        hx, hy = home[i]
        for j in range(len(selected)):
            cx, cy = selected[j]
            temp = abs(hx-cx) + abs(hy-cy)
            cnt = min(cnt, temp)
        dis += cnt
    res = min(res, dis)


sel_chicken(0, 0)
print(res)
