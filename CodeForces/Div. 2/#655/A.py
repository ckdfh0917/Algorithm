T = int(input())

for _ in range(T):
    n = int(input())
    res = []
    for i in range(1, 1001, 2):
        res.append(i)
        if len(res) == n:
            break

    print(' '.join(map(str, res)))