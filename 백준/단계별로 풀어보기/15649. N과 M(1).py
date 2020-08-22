N, M = map(int, input().split())

def f(n):
    c = len(ans)
    # print(n)
    if c == M:
        return print(' '.join(map(str, ans)))
    else:
        for i in range(1, N+1):
            if not visited[i]:
                ans.append(i)
                visited[i] = 1
                f(i)
                ans.pop()
                visited[i] = 0
ans = []
visited = [0] * (N+1)
f(1)