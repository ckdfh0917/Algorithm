munja = input()

arr = [0] * 26

for i in range(len(munja)):
    if ord(munja[i]) >= 97:
        temp = ord(munja[i]) - 97
        arr[temp] += 1
    elif ord(munja[i]) >= 65:
        temp = ord(munja[i])-65
        arr[temp] += 1

maxV = 0
maxI = 0

for i in range(len(arr)):
    if maxV < arr[i]:
        maxV = arr[i]
        maxI = i

if arr.count(maxV) > 1:
    print('?')
else:
    result = chr(maxI + 65)
    print(result)