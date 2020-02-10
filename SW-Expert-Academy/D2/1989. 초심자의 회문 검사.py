q = int(input())

for test_case in range(1, q + 1):
    munja = input()

    flag = 1
    if len(munja) % 2 == 0:
        for i in range(len(munja) // 2):
            if munja[i] != munja[-1 - i]:
                flag = 0

    else:
        for i in range(len(munja) // 2):
            if munja[i] != munja[-1 - i]:
                flag = 0

    print('#{} {}'.format(test_case, flag))