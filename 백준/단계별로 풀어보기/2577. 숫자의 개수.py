A = int(input())
B = int(input())
C = int(input())

D = A * B * C
D = str(D)
a = [0] * 10
for i in D:
    a[int(i)] += 1

for i in range(10):
    print(a[i])