q = int(input())

for test_case in range(1, q + 1):
    munja = input()

    for i in range(1, 30):
        if munja[0] == munja[i]:
            if munja[0:i] == munja[i:2 * i]:
                print('#{} {}'.format(test_case, i))
                break