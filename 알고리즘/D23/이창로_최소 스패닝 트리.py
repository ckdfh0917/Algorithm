import heapq
T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    py = p[find_set(y)]
    px = p[find_set(x)]
    if px > py:
        p[py] = px
    else:
        p[px] = py

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        s, e, n = map(int, input().split())
        adj[s].append([e, n])
        adj[e].append([s, n])

    print(adj)

    INF = float('inf')
    key = [INF] * V
    mst = [False] * V
    pq = []
    key[0] = 0
    p = [i for i in range(V+1)]

    heapq.heappush(pq, (0,0))

    print(p)
    while pq:
        k, node = heapq.heappop(pq) # 우선순위가 가장 높은 것을 가져옴
        mst[node] = True
        for dest, wt in adj[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
