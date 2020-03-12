n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
c = [0] * n
for i in range(n):
    c[i] = a[i] - b[i]

c.sort()
for i in range(n):
    if c[i] > 0:
        cnt += (n-i) * (n-i-1) // 2
        break
    for j in range(i+1,n):
        temp = c[i] + c[j]
        if temp > 0:
            cnt += n-j
            break
print(cnt)


def f(a, minV, maxV):
    if a + c[(minV+maxV)//2] > 0:
        return (minV+maxV)//2
    else:
        if a + c[(minV+maxV)//2]:
            pass


for i in range(n):
    f(i, 2, 2*(10**5))