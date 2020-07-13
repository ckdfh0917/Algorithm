N = int(input())

numbers = list(map(int, input().split()))

cnt = 0
for i in range(1, N):
    numbers[i] = numbers[i] + numbers[i-1]

print(sum(numbers))