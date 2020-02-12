q = int(input())

for test_case in range(1, q + 1):
    num = int(input())
    a2, a3, a5, a7, a11 = 0, 0, 0, 0, 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            a2 += 1
        elif num % 3 == 0:
            num = num // 3
            a3 += 1
        elif num % 5 == 0:
            a5 += 1
        elif num % 7 == 0:
            a7 += 1
        elif num % 11 == 0:
            a11 += 1

    print('#{} {} {} {} {} {}'.format(test_case, a2, a3, a5, a7, a11))