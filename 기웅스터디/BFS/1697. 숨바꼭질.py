import sys
input = sys.stdin.readline
n, k = map(int, input().split())
q = []
visited = [0] * 100001

def bfs(n, k):
    q.append([n, 0])
    visited[n] = 1

    while q:
        # print(q)
        a, b = q.pop(0)

        if a == k:
            return b

        if a + 1 < 100001 and visited[a+1] == 0:
            q.append([a+1, b+1])
            visited[a+1] = 1
        if a - 1 >= 0 and visited[a-1] == 0:
            q.append([a-1, b+1])
            visited[a-1] = 1
        if a * 2 < 100001 and visited[a*2] == 0:
            q.append([a*2, b+1])
            visited[a*2] = 1


print(bfs(n, k))
