q = int(input())

for test_case in range(1, q + 1):
    len_num = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort()

    str_num = str(numbers)

    new_num = str_num.replace('[', '')
    new_num = new_num.replace(']', '')
    new_num = new_num.replace(',', '')

    print('#{} {}'.format(test_case, new_num))
