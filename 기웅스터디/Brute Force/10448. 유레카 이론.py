T = int(input())

dp = [0] + [0] * 50
for i in range(1, 50):
    dp[i] = dp[i - 1] + i

for _ in range(T):
    n = int(input())

    # print(dp)
    a = []
    flag = 0
    for i in range(1,len(dp)-1):
        for j in range(1,len(dp)-1):
            for k in range(1,len(dp)-1):
                # print(dp[i], dp[j] , dp[k], n)
                if dp[i] + dp[j] + dp[k] == n:
                    print(1)
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:
            break

    if flag == 0:
        print(0)