import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
q = deque([])
visited = [0] * 100001

def f(x, y):
    # print(x, y)
    res = 100000
    if x > y:
        return print(x-y)
    elif x == y:
        return print(0)
    else:
        q.append([y, 0])
        visited[y] = 1
        while q:
            print(q)
            t, cnt = q.popleft()
            visited[t] = 1
            print(t, cnt)
            if t == x:
                res = min(res, cnt)
                print(res)
                break
            else:
                if t % 2 == 0:
                    if visited[t//2] == 0:
                        q.append([t//2, cnt+1])
                else:
                    if visited[t-1] == 0:
                        q.append([t-1, cnt+1])
                    if visited[t+1] == 0:
                        q.append([t+1, cnt+1])
    if res == 100000:
        pass
    print(res)
f(a, b)
