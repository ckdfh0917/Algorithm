import sys
sys.setrecursionlimit(10**9)
N = int(input())

arr = [[] * (N+1) for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# print(arr)

visited = [0] * (N+1)
ans = [0] * (N+1)

def dfs(x):
    visited[x] = 1
    # print(x)
    if 0 not in visited:
        return
    else:
        for i in arr[x]:
            # print('a', i)
            if visited[i] == 0:
                ans[i] = x
                dfs(i)
    return

dfs(1)
# print()
for i in range(2, N+1):
    print(ans[i])