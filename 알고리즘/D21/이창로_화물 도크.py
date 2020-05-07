T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))

    t = sorted(time, key=lambda x: (x[1],x[0]))
    checked = [0] * 25
    res = 0
    for i in range(N):
        start = t[i][0]
        end = t[i][1]
        if 1 not in checked[start:end+1]:
            res += 1
            while start < end:
                checked[start] = 1
                start += 1
    print('#{} {}' .format(test_case, res))