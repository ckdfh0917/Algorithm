q = int(input())

for test_case in range(1, q + 1):
    result = 0

    numbers = list(map(int, input().split()))

    numbers.sort()

    result = 0
    for i in numbers:
        result += i

    result = result - numbers[0] - numbers[9]
    result = result / 8
    result = round(result)

    print('#{} {}'.format(test_case, result))