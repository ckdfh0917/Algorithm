from sys import stdin
N = int(stdin.readline())
A = sorted(list(map(int,stdin.readline().split())))
M = int(stdin.readline())
B = list(map(int,stdin.readline().split()))

def f(x):
    s = 0
    e = N - 1

    while s <= e:
        mid = (s+e) // 2
        if A[mid] == x:
            return A[s:e+1].count(x)
        else:
            if A[mid] < x:
                s = mid + 1
            else:
                e = mid - 1
    return 0

res = {}

for n in B:
    if n not in res:
        res[n] = f(n)
# print(res)
print(' '.join(str(res[x]) if x in res else '0' for x in B))