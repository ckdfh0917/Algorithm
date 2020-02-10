# 0 이면 문자열의 맨앞으로 - 추가
# 0 이 아니면 문자열의 인덱스에 - 추가

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q + 1):
    munja = list(input())
    num = int(input())
    space = list(map(int, input().split()))
    print('#{} ' .format(test_case) ,end='')

    temp = 0
    for i in space:
        if i == 0:
            munja[i] = '-' + munja[i]
        else:
            munja[i-1] += '-'
        print(munja)
    print(''.join(munja))
