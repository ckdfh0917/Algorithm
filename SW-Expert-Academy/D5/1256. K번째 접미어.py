q = int(input())

for test_case in range(1,q+1):
    n = int(input())
    munja = list(input())
    print('#{} '.format(test_case), end='')

    new_munja = []
    for i in range(len(munja)):
        new_munja.append(''.join(munja[i:]))

    new_munja.sort()
    print(new_munja[n-1])