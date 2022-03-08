arr = input()
temp = 0
res = 0
for a in arr:
    if a != temp:
        res += 10
        temp = a
    else:
        res += 5

print(res)