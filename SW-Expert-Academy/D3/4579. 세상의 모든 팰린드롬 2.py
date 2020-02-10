# 1과의 차이는 *가 있으면 0이상의 문자를 대입하는 것이 가능
# 결국 *이 하나라도 있으면 팰린드롬을 만들 수 있다는 것이됨

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q + 1):
    munja = list(input())

    print('#{} '.format(test_case), end='')

    flag = 0
    for i in range(len(munja) // 2):
        if munja[i] == munja[len(munja)-1-i]:
            continue
        elif munja[i] == '*' or munja[len(munja)-i-1] == '*':
            break
        else:
            print('Not exist')
            flag = 1
            break
    if flag == 0:
        print('Exist')