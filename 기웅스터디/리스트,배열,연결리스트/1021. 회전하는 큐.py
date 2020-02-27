N, M = map(int, input().split())
numbers = list(map(int, input().split()))
P = N
temp = 0
cnt = 0
# print('a')
for i in range(M):
    print('i', i, numbers[i], temp, numbers[i] + temp)
    while True:
        if numbers[i] + temp > N:
            numbers[i] = (numbers[i]) - N
        else:
            break
    while True:
        if numbers[i] + temp < 1:
            a = numbers[i] + temp + 1 + 1
            numbers[i] = -temp + numbers[i] + temp + P -1
        else:
            break
    print('================================')
    print('i2', i, numbers[i], temp, numbers[i] + temp)

    while True:
        print('q', numbers[i], temp)

        if numbers[i] + temp == 1:
            temp -= 1
            N -= 1
            break
        if numbers[i]+temp <= N // 2 + 1:
            temp -= 1
            if numbers[i] + temp < 1:
                numbers[i] = N - temp
            cnt += 1
        else:
            temp += 1
            if numbers[i] + temp > N:
                numbers[i] = -temp + 1
            cnt += 1
        print('p', numbers[i] + temp, N, end=' ')
        print('c',cnt)

print(cnt)