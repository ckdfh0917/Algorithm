from collections import deque
N = int(input())


arr = [[0] * 101 for _ in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def generate(d, g, c):
    gen.append(d)

    while c < g:
        if g == c:
            return
        temp = []
        for i in range(len(gen)-1, -1, -1):
            if gen[i]+1 == 4:
                temp.append(0)
            else:
                temp.append(gen[i]+1)

        gen.extend(temp)
        c += 1

for _ in range(N):
    x, y, d, g = map(int, input().split())
    gen = []
    generate(d, g, 0)
    arr[y][x] = 1
    while gen:
        d = gen.pop(0)
        x = x+dx[d]
        y = y+dy[d]
        arr[y][x] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1]:
            ans += 1

print(ans)


