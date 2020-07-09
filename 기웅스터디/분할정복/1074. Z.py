z = list(map(int, input().split()))
N, r, c = z[0], z[1], z[2]

n = 2 ** N

def f(x, y, a):
    global result
    # print(x, y, a)
    if x == r and y == c:
        print(result)
        return
    if a == 1:
        result += 1
        return

    if not(x <= r and r < x+a and y <= c and c < y+a):
        result += a * a
        return
    f(x, y, a//2)
    f(x, y+a//2, a//2)
    f(x+a//2, y, a//2)
    f(x+a//2, y+a//2, a//2)

result = 0

f(0, 0, n)
