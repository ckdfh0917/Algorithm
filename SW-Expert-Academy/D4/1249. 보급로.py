import heapq

T = int(input())

MAX = 1234567891
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    heap = []
    heapq.heappush(heap, (dist[0][0], 0, 0))
    while heap:
        d, x, y = heapq.heappop(heap)
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
                nd = d + arr[x+dx[i]][y+dy[i]]
                if dist[x+dx[i]][y+dy[i]] > d + arr[x+dx[i]][y+dy[i]]:
                    dist[x + dx[i]][y+dy[i]] = dist[x][y]+arr[x+dx[i]][y+dy[i]]
                    heapq.heappush(heap, (dist[x+dx[i]][y+dy[i]], x+dx[i], y+dy[i]))


for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dist = [[MAX] * N for _ in range(N)]
    dist[0][0] = 0

    bfs()
    print('#{} {}'.format(test_case, dist[N-1][N-1]))
