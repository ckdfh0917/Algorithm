t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    visited = [0] * n

    cnt = 0
    for i in range(len(q)):
        if visited[i] == 0:
            cnt += 1
            visited[i] = 1

