T = int(input())

def bfs(k, v, cnt):
    global minV
    q = []
    for i in range(k+1, V+1):
        if v[i] == 0 and arr[k][i] != 0:
            q.append([k,i])
            v[i] = 1
    while q:
        a, b = q.pop(0)
        cnt += arr[a][b]
        print(a,b, cnt)
        if cnt >= minV:
            return

        for j in range(V + 1):
            if v[j] == 0 and arr[b][j] != 0:
                q.append([b, j])
                v[j] = 1
    print(k, v, cnt)
    if 0 not in v:
        minV = min(minV, cnt)
    return


for test_case in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        n = list(map(int, input().split()))
        arr[n[0]][n[1]] = n[2]
        arr[n[1]][n[0]] = n[2]

    for i in range(V+1):
        print(arr[i])

    minV = 1234567891
    for i in range(V+1):
        visited = [0] * (V+1)
        visited[i] = 1
        bfs(i,visited, 0)
    print(minV)