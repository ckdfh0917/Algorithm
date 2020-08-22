n = int(input())

k = []
a = 1
i = 0
while a < n:
    a += 6 * i
    k.append(a)
    i += 1
# print(k)
if n == 1:
    print(1)
else:
    for i in range(len(k)-1):
        if k[i] < n <= k[i+1]:
            # print(k[i], n, k[i+1])
            print(i+2)