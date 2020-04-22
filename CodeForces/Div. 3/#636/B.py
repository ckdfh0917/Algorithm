t = int(input())

for _ in range(t):
    n = int(input())
    result = []

    if (n // 2) % 2 == 0:
        print('YES')
        for i in range(1, n+1):
            if i % 2 == 0:
                result.append(i)

        for i in range(1, n-1):
            if i % 2 == 1:
                result.append(i)
        a = sum(result[:n//2])
        b = sum(result[n//2:])
        result.append(a-b)

        print(' '.join(map(str, result)))

    elif (n // 2) % 2 == 1:
        print('NO')