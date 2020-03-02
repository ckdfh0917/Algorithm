n = int(input())
a, b = map(int, input().split())
m = int(input())

Q = []
lst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
print(lst)

def bfs(k):
    visited[k] = True
    Q = [k]
    flag = 0
    res = 0
    while Q:
        curr = Q.pop(0)
        if flag == 0:
            for next in lst[curr]:
                print('a',next, visited)
                if next == a:
                    flag = 1
                    for i in range(len(visited)):
                        visited[i] = False
                if not visited[next]:
                    visited[next] = True
                    Q.append(next)
        if flag == 1:

            if flag == 1 and next == b:
                return res

    return -1

print(bfs(1))
