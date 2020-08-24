N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

p = [0] * N * N

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
    p[py] = px

    # for i in range(N*N):
    #     if py == find_set(i):
    #         p[i] = px

# 연합한 국가 인구수 더하기 및 연합 나라 숫자 세기
def check():
    visited = [[0] * N for _ in range(N)]

    c = 0
    for i in range(N):
        for j in range(N):
            make_set(c)
            c += 1

    man = [0] * (N*N)
    flag = False
    for i in range(N):
        for j in range(N):
            cnt = (N) * (i) + j
            T = find_set(cnt)
            # print('cnt', cnt, T)
            for k in range(4):
                # print('ii', i+dx[k], j+dy[k])
                if 0 <= i+dx[k] < N and 0 <= j+dy[k] < N:
                    if L <= abs(arr[i][j] - arr[i+dx[k]][j+dy[k]]) <= R:
                        flag = True
                        if k == 0:
                            if T != find_set(cnt-N):
                                print('c', cnt, cnt+1, find_set(cnt), find_set(cnt-N))
                                union(cnt, cnt-N)
                                print(k, p)
                        elif k == 1:
                            if T != find_set(cnt+1):
                                print('c', cnt, cnt+1, find_set(cnt), find_set(cnt+1))
                                union(cnt, cnt+1)
                                print(k, p)
                        elif k == 2:
                            if T != find_set(cnt+N):
                                print('c', cnt, cnt+1, find_set(cnt), find_set(cnt+N))
                                union(cnt, cnt+N)
                                print(k, p)
                        elif k == 3:
                            if T != find_set(cnt-1):
                                print('c', cnt, cnt+1, find_set(cnt), find_set(cnt-
                                                                               1))
                                union(cnt, cnt-1)
                                print(k, p)

    if flag:
        print('ppp', p)
        cnt = 0
        for i in range(N):
            for j in range(N):
                man[p[cnt]] += arr[i][j]
                cnt += 1

        print('mmmm', man)
        cnt = 0
        for i in range(N):
            for j in range(N):
                if p.count(p[cnt]) > 1:
                    temp = man[p[cnt]] // p.count(p[cnt])
                    arr[i][j] = temp

                cnt += 1
        for i in range(N):
            print(arr[i])
        return True
    else:
        return False

res = 0
while check():
    res += 1

print(res)