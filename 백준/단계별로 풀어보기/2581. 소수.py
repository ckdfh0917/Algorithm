M = int(input())
N = int(input())

def sosu(n):
    for i in range(2,n+1):
        if a[i] == 1:
            b.append(i)
            for j in range(i*2,n+1,i):
                a[j] = 0

a = [0] + [0] + [1] * (N-1)
b = []
sosu(N)
# print(a)
# print(b)

res = []
for x in b:
    if M <= x:
        res.append(x)
# print(res)

if not res:
    print(-1)
else:
    print(sum(res))
    print(min(res))