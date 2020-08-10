N = int(input())

days = [[-1, -1]] + [[] for _ in range(N)]
for i in range(1, N+1):
    days[i] = list(map(int, input().split()))

maxV = 0
def dfs(x, res):
    global maxV
    for i in range(x+1, N+1):
        if i + days[i][0] - 1 < N+1:
            dfs(i+days[i][0]-1, res+days[i][1])
    maxV = max(res, maxV)
    return

for i in range(1, N+1):
    if i + days[i][0]-1 < N+1:
        dfs(i+days[i][0]-1, days[i][1])
print(maxV)