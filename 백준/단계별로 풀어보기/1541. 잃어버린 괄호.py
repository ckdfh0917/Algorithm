N = input().split('-')
result = 0

for i in N[0].split('+'):
    result += int(i)

for i in N[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)