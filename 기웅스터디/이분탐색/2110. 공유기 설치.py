n, c = map(int, input().split())

home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

def possi(a):
    cnt = 0
    pre = 10 ** -9
    for i in range(N):
        