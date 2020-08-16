N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split()))

def op(a, b, c, d, cnt, ans):
    global maxV, minV
    if cnt == N-1:
        minV = min(minV, ans)
        maxV = max(maxV, ans)
        return

    if a > 0:
        op(a-1, b, c, d, cnt+1, ans+A[cnt+1])
    if b > 0:
        op(a, b-1, c, d, cnt+1, ans-A[cnt+1])
    if c > 0:
        op(a, b, c-1, d, cnt+1, ans*A[cnt+1])
    if d > 0:
        if ans > 0:
            temp = ans // A[cnt+1]
        else:
            t = ans * -1
            temp = t // A[cnt+1]
            temp *= -1
        op(a, b, c, d-1, cnt+1, temp)

    return


maxV = -1000000000
minV = 1000000000

op(cal[0], cal[1], cal[2], cal[3], 0, A[0])
print(maxV)
print(minV)