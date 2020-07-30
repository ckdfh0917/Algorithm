numPC = int(input())
n = int(input())

arr = [[0] * (numPC+1) for _ in range(numPC+1)]
dp = [[0] * (numPC+1) for _ in range(numPC+1)]

for _ in range(n):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1


stack = []
def dfs(x):
    for i in range(1, numPC):
        arr[x][i]