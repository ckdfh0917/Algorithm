q = int(input())

for test_case in range(1, q + 1):
    result = 0

    numbers = int(input())

    for i in range(1, numbers + 1):
        if i % 2 == 1:
            result = result + i
        elif i % 2 == 0:
            result = result - i

    print('#{} {}'.format(numbers, result))