N = int(input())
parent = list(map(int, input().split()))
target = int(input())

tree = [[-1] * N for _ in range(N)]

root = -1

for i in range(N):
    if parent[i] == -1:
        root = i
        continue
    tree[i][parent[i]] = i
    tree[parent[i]][i] = i

# for i in range(N):
#     print(tree[i])

tree[target][parent[target]] = -1
tree[parent[target]][target] = -1

# print('============================')
# for i in range(N):
#     print(tree[i])

cnt = 0


def dfs(idx):
    global cnt

    # print(idx)

    flag = False
    for i in range(N):
        if tree[idx][i] != -1:
            flag = True
            tree[idx][i] = -1
            tree[i][idx] = -1
            dfs(i)

    if not flag:
        cnt += 1
        return

# print('root', root)
if root == target:
    print(0)
else:
    dfs(root)
    print(cnt)
