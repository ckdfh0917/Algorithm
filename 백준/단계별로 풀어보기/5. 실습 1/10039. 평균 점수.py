temp = 0
for i in range(5):
    k = int(input())
    if k < 40:
        k = 40
    temp += k
print(temp // 5)
