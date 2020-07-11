N = int(input())

numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

temp = [0] * N
for i in range(N):
    x, y = numbers[i]
    cnt = 0
    for j in range(N):
        if i != j:
            a, b = numbers[j]
            if x < a and y < b:
                cnt += 1
    temp[i] = cnt


res = [0] * N
cnt = 1
for i in range(N):
    temp[i] += 1

print(' '.join(map(str, temp)))