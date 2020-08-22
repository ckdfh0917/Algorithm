N, M = map(int, input().split())

def f():
    c = len(ans)
    if c == M:
        return print(' '.join(map(str, ans)))
    else:
        for i in range(1, N+1):
            ans.append(i)
            f()
            ans.pop()

ans = []
f()