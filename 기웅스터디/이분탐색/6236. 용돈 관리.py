N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

# print(money)

def f(i, m, a, minV, maxV):
    # print(i,m,a,(minV+maxV)//2)
    global res
    if i == N:
        # print()
        if m > M:
            f(1, 1, money[0], (minV+maxV)//2, maxV)
        elif m < M:

            f(1, 1, money[0], minV, (minV+maxV)//2)
        elif m == M:
            res = min(res, (minV+maxV)//2)
        return
    else:
        a += money[i]
        if a > (minV+maxV)//2:
            f(i+1, m+1, 0, minV, maxV)
        elif a == (minV+maxV)//2:
            f(i,m+1,0, minV, maxV)
        else:
            f(i+1, m, a, minV, maxV)

res = 100000
f(1,1,money[0],max(money),100000)
print(res)