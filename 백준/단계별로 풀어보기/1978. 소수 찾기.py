n = int(input())
num = list(map(int, input().split()))


def sosu(n):
    for i in range(2,n):
        if a[i] == 1:
            for j in range(i*2,n,i):
                a[j] = 0

a = [0] + [0] + [1] * (1000-2)
sosu(1000)

b = []
for i in range(1000):
    if a[i] == 1:
        b.append(i)
# print(b)

cnt = 0
for x in num:
    for y in b:
        if x == y:
            cnt += 1
            break
print(cnt)