import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q + 1):
    munja = list(input())

    print('#{} '.format(test_case),end='')
    #print(munja)

    flag = 0
    for i in range(len(munja) // 2):
        if munja[i] == munja[len(munja)-1-i]:
            continue
        elif munja[i] == '?' or munja[len(munja)-i-1] == '?':
            continue
        else:
            print('Not exist')
            flag = 1
            break
    if flag == 0:
        print('Exist')