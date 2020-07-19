N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

res1 = sum(numbers) / N
res2 = sorted(numbers)
res3 = {}
res4 = max(numbers) - min(numbers)

print(round(res1))
print(res2[N//2])

new_num = [0] * 9000

for i in range(N):
    new_num[numbers[i]+4000] += 1

maxV = max(new_num)

if new_num.count(maxV) == 1:
    print(new_num.index(maxV)-4000)
else:
    flag = 0
    for i in range(len(new_num)):
        if new_num[i] == maxV:
            if flag == 0:
                flag += 1
            else:
                print(i - 4000)
                break

print(res4)