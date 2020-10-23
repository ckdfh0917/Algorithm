test_case = 0

# dfs를 통해 정점 개수 파악
def num_of_node(idx):
    cnt = 1
    visited[idx] = 1
    # print(idx, visited)

    for i in range(len(tree[idx])):
        next = tree[idx][i]
        # print('next', next)
        if visited[next] == 0:
            k = num_of_node(next)
            cnt += k
            # print('kk', next, k, cnt)
    return cnt

def num_of_edge(idx):
    cnt = len(tree[idx])
    passed[idx] = 1

    for i in range(len(tree[idx])):
        next = tree[idx][i]
        if not passed[next]:
            cnt += num_of_edge(next)

    return cnt

while True:
    test_case += 1
    n, m = map(int, input().split())

    if n == m == 0:
        break

    p = [x for x in range(n+1)]
    tree = [[] * (n+1) for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [0] * (n+1)
    passed = [0] * (n+1)
    visited[0] = 1
    passed[0] = 1
    result = 0

    for i in range(1, n+1):
        if not visited[i]:
            V = num_of_node(i)
            E = num_of_edge(i)

            # print('ve', V, E)
            if V-1 == E / 2:
                result += 1

    if result == 0:
        print('Case {}:'.format(test_case), 'No trees.')
    elif result == 1:
        print('Case {}:'.format(test_case), 'There is one tree.')
    elif result > 1:
        print('Case {}:'.format(test_case), 'A forest of {} trees.'.format(result))

