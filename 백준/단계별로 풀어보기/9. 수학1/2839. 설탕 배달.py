# while True:
N = int(input())

a = N // 5
b = N
cnt = 1
res = a*2 + 100
temp2 = a+2 + 100
for i in range(0,a+1):
    b = N - i * 5
    c = b // 5
    d = b % 5
    # print('b',b,c,d)
    if d == 0:
        res = a - i
        # print(res)

        break

    if b % 3 == 0:
        temp2 = i + (b // 3)
        # print('t',temp2, i, b//3, temp)
        continue
if res < temp2:
    res = res
else:
    res = temp2

if res == a*2 + 100:
    res = -1
print(res)
