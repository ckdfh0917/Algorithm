y = int(input())

if y % 4 == 0:
    if y % 400 == 0:
        result = 1
    elif y % 100 == 0:
        result = 0
    else:
        result = 1
else:
    result = 0
print(result)