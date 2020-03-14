import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

# print(money)

minV = 1
maxV = sum(money)
res = maxV
while minV <= maxV:
    temp = (minV+maxV)//2
    cnt = 1
    flag = 0
    # print('b',(cnt, minV, maxV, (minV+maxV)//2))
    for i in range(N):
        if (minV+maxV)//2 < money[i]:
            flag = 1
            break
        if temp - money[i] < 0:
            temp = (minV+maxV)//2
            cnt += 1
        temp -= money[i]

        # print(cnt, temp)
    if flag == 0:
        if cnt <= M:
            res = min(res, (minV+maxV)//2)
            # print('r', res)
            minV = minV
            maxV = (minV + maxV) // 2 - 1
        else:
            minV = (minV + maxV) // 2 + 1
            maxV = maxV
    elif flag == 1:
        minV = (minV+maxV)//2 + 1
print(res)