import heapq
T = int(input())

def cal(x1, y1, x2, y2, E):
    return ((x1-x2)**2 + (y1-y2)**2) * E

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x:
        return p[x]
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    py = find_set(p[y])
    px = find_set(p[x])

    p[py] = px

for test_case in range(1, T+1):
    N = int(input()) # 섬의 개수
    # 섬의 좌표들
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    distance = []
    for i in range(N):
        for j in range(i+1, N):
            heapq.heappush(distance, (cal(X[i], Y[i], X[j], Y[j], E), i, j))

    # print(distance)
    p = [0] * (N+1)
    for i in range(N+1):
        make_set(i)

    cnt = 0
    ans = 0
    while cnt < N-1:
        d, a, b = heapq.heappop(distance)
        if find_set(a) == find_set(b):
            continue
        else:
            union(a, b)
            ans += d
            cnt += 1

    res = round(ans)
    print('#{} {}' .format(test_case, res))