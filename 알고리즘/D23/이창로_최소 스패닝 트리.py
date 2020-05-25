import heapq
T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    py = p[find_set(y)]
    px = p[find_set(x)]
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [list(map(int, input().split())) for i in range(E)]

    # for i in range(E):
    #     print(adj[i])
    # 간선을 간선가중치를 기준으로 정렬
    adj.sort(key=lambda x: x[2])

    # make_set: 모든 정점에 대해 집합 생성
    p = [0] * (V+1)
    rank = [0] * (V+1)
    for i in range(V+1):
        make_set(i)
    cnt = 0
    result = 0
    mst = []
    # 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때 까지
    for i in range(E):
        s, e, c = adj[i][0], adj[i][1], adj[i][2]
        # 사이클이면 스킵 : 간선의 두 정점이 서로 같은 집합이면 => find_set
        if find_set(s) == find_set(e):
            continue
        # 간선 선택
        # => mst에 간선 정보 더하기 / 두 정점 합치기 => union
        result += c
        mst.append(adj[i])
        union(s, e)

        cnt += 1
        if cnt == V-1: break
    print('#{} {}'.format(test_case, result))
