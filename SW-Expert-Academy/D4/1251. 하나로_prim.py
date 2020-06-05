import heapq
T = int(input())

def prim(s):
    ans = 0

    key[s] = 0
    heapq.heappush(pq, (key[s], s))

    while pq:
        dist, u = heapq.heappop(pq)
        if visitied[u] == 1:
            continue
        else:
            visitied[u] = 1
            ans += dist

            for i in range(N):
                if visitied[i] == 0 and arr[i][u] < key[i]:
                    key[i] = arr[i][u]
                    heapq.heappush(pq, (key[i], i))
    res = round(ans)
    return res


def cal(x1, y1, x2, y2, E):
    return ((x1-x2)**2 + (y1-y2)**2) * E

for test_case in range(1, T+1):
    N = int(input()) # 섬의 개수
    # 섬의 좌표들
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    pq = []
    key = [1234567891123456789] * N
    visitied = [0] * N
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            arr[i][j] = cal(X[i], Y[i], X[j], Y[j], E)
            arr[j][i] = cal(X[i], Y[i], X[j], Y[j], E)

    print('#{} {}'.format(test_case, prim(0)))