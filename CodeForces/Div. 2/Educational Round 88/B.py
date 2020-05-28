T = int(input())

for _ in range(T):
    n, m, x, y = map(int, input().split())

    arr = [input() for _ in range(n)]
    # for i in range(n):
    #     print(arr[i])
    # print()

    res = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == '*':
                if cnt == 1:
                    res += x
                cnt = 0
            elif arr[i][j] == '.':
                cnt += 1
                if cnt == 2:
                    if x * 2 < y:
                        res += x * 2
                    else:
                        res += y
                    cnt = 0
        if cnt == 1:
            res += x
    print(res)