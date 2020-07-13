N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))


# print(numbers)
numbers.sort()
for i in range(N):
    print(numbers[i])