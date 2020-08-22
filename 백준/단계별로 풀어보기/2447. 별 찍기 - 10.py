N = int(input())
star = [[' '] * N for _ in range(N)]

def f(x, y, n):
    if n == 3:
        for i in range(3):
            for j in range(3):
                star[x+i][y+j] = '*'
        star[x+1][y+1] = ' '
    else:
        f(x, y, n//3)
        f(x+n//3, y, n//3)
        f(x+2*n//3, y, n//3)
        f(x, y+n//3, n//3)
        f(x+2*n//3, y+n//3, n//3)
        f(x, y+2*n//3, n//3)
        f(x+n//3, y+2*n//3, n//3)
        f(x+2*n//3, y+2*n//3, n//3)
f(0,0,N)
for i in range(N):
    print(''.join(map(str, star[i])))