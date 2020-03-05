q = int(input())

dx = [-1,0,1,0] # 위 오른 아래 왼
dy = [0,1,0,-1]

def find(i,j,n,s):
    if n == 7:
        t.add(s)
    else:
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < 4 and 0 <= nj <4:
                find(ni, nj, n+1, s+str(a[i][j]))

for test_case in range(1, q+1):
    a = [list(map(int, input().split())) for i in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            find(i, j, 0, '')
    print('#{} {}'.format(test_case, len(t)))