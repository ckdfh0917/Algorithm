data = [-7,-3,-2,5,8]

n = len(data)
ans = False
for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i & (1<<j):
            sum += data[j]
    if sum == 0:
        ans = True
        break
print(ans)