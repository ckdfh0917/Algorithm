dx = [0,0,1,0,-1]            # 나 오 아래 왼 위
dy = [0,1,0,-1,0]

def snail(n):
    arr = [[0] * (n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i == 0 or i == n+1:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
            if j == 0 or j == n+1:
                arr[i][j] = 1
    for i in range(n+2):
        print(arr[i])
    print('-------------')

    x, y = 1, 1
    for i in range(n**2):
        for k in range(5):
            if arr[x+dx[k]][y+dy[k]] == 0:
                arr[x+dx[k]][y+dy[k]] = i+1
                x = x+dx[k]
                y = y+dy[k]
                for a in range(n + 2):
                    print(arr[a])
                print('-------------')
                break
    return arr

n = int(input())
arr = snail(n)

for i in range(1,n+1):
    arr[i].pop(0)
    arr[i].pop()
    print(' '.join(map(str,arr[i])))
