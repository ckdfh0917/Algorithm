from collections import deque
N = int(input())
M = int(input())

arr = [[0] * N for _ in range(N)]

q = deque()
q.append(N)
for i in range(N-1):
    q.append(N-1-i)
    q.append(N-1-i)

cnt = N * N
for p in range((N-1)//2):
    a1 = q.popleft()
    a2 = q.popleft()
    a3 = q.popleft()
    a4 = q.popleft()

    # down
    for k in range(a1):
        arr[p+k][p] = cnt
        cnt -= 1

    # right
    for k in range(a2):
        arr[N-p-1][p+k+1] = cnt
        cnt -= 1

    # up
    for k in range(a3):
        arr[N-p-2-k][N-p-1] = cnt
        cnt -= 1

    # left
    for k in range(a4):
        arr[p][N-p-2-k] = cnt
        cnt -= 1
arr[N//2][N//2] = 1

x, y = 0, 0
for i in range(N):
    string = ""
    for j in range(N):
        string += str(arr[i][j]) + " "
        if arr[i][j] == M:
            x = i + 1
            y = j + 1
    print(string)
    # print(arr[i])
print(x, y)