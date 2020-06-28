T = int(input())

for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    temp = 0
    dp = [0] * (len(num) + 1)
    for i in range(len(num)-1, -1, -1):
        if temp == 0:
            temp = num[i]
            dp[i] = 1
        else:
            if temp < num[i]:
                temp = num[i]
                dp[i] = 1

    # print(dp)

    cnt = 0
    point = 0
    for i in range(len(dp)-1, -1, -1):
        if dp[i] == 1:
            point = num[i]
        else:
            if point == 0:
                continue
            cnt += point - num[i]
    print(cnt)