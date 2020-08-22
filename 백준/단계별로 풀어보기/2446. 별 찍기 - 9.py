n = int(input())

for i in range(n, 0, -1):
    t = ' ' * (n - i) + '*' * (2 * i - 1)
    print(t)
for i in range(2, n+1):
    t = ' ' * (n - i) + '*' * (2 * i - 1)
    print(t)