import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

k = ['a','e','i','o','u']

for test_case in range(1, q+1):
    munja = list(input())
    print('#{} '.format(test_case), end='')
    #print(munja)
    res = []
    for i in range(len(munja)):
        if munja[i] not in k:
            res.append(munja[i])
    print(''.join(res))

