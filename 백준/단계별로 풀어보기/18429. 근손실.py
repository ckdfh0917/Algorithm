# N, M = map(int, input().split())
# kit = list(map(int, input().split()))
# visited = [0] * N
# ans = 0
#
#
# def dfs(idx, w, cnt):
#     global ans
#
#     w += kit[idx] - M
#     if w < 500:
#         return
#
#     ##print("##", idx, w, cnt)
#     if cnt >= N:
#         ans += 1
#         return
#     ##print(idx, kit[idx], w)
#
#     for j in range(N):
#         if idx == j or visited[j] == 1:
#             continue
#         visited[j] = 1
#         ##print("------------")
#         ##print("j : ", j, visited)
#         dfs(j, w , cnt+1)
#         visited[j] = 0
#
#     return
#
#
# for i in range(N):
#     ##print("=================")
#     ##print("i : ", i)
#     visited[i] = 1
#     dfs(i, 500, 1)
#     visited[i] = 0
#
# print(ans)

import itertools

N, K = map(int, input().split())
kit = list(map(int, input().split()))
permutation = itertools.permutations(kit, N)
ans = 0

for per in permutation:
    w = 0
    for p in per:
        w += p - K
        if w < 0:
            break
    if w >= 0:
        ans += 1

print(ans)

