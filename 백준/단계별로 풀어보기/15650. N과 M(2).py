N, M = map(int, input().split())

def f(n):
    c = len(ans)
    if c == M:
        return print(' '.join(map(str, ans)))
    else:
        for i in range(n+1, N+1):
            ans.append(i)
            f(i)
            ans.pop()

ans = []
f(0)