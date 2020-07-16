N = int(input())
numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

numbers.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(' '.join(map(str, numbers[i])))
