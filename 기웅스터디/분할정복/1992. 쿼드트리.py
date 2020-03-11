N = int(input())
tree = [list(input()) for _ in range(N)]
# for i in range(N):
#     print(tree[i])

temp = ''
def f(x, y, n):
    global temp
    # print(temp)
    a = tree[x][y]
    if n == 1:
        # print('a')
        temp += a
        return
    flag = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tree[i][j] != a:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        # print('b')
        temp += a
    elif flag == 1:
        temp += '('
        f(x, y, n//2)
        f(x, y + n//2, n//2)
        f(x + n//2, y, n//2)
        f(x + n//2, y + n//2, n//2)
        temp += ')'
f(0,0,N)
print(temp)
