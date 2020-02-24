num = int(input())

# DP = [[0] * 3 for _ in range(10**6)]
visited = [[0] * 3 for _ in range(10**6)]

result = 10**6
k = 0
while True:
    k += 1
    cnt = 0
    N = num
    # print('a', N)
    for i in range(10**6):
        if N % 3 == 0 and visited[i][0] == 0:      # 1번 명령어
            N //= 3
            visited[i][0] = 1
        elif N % 2 == 0 and visited[i][1] == 0:    # 2번 명령어
            N //= 2
            visited[i][1] = 1
        elif visited[i][2] == 0:   # 3번 명령어
            N -= 1
            visited[i][2] = 1
        # print('b', N)
        if N == 1:
            cnt = i + 1
            break
        if N == num:
            break
    # print(visited)
    if result > cnt and cnt != 0:
        result = cnt
    # print(i)
    if k > num:
        break
print(result)