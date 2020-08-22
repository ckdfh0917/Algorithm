max_V = 0
max_I = 0
for i in range(1,10):
    k = int(input())
    if max_V < k:
        max_V = k
        max_I = i
print(max_V)
print(max_I)