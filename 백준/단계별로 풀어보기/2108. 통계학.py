N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

res1 = sum(numbers) / N
res2 = {}
res3 = 0
res4 = max(numbers) - min(numbers)


for i in range(N):
    res2[numbers[i]] = numbers.count(numbers[i])

print(res2)
