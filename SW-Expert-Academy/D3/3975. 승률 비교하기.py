# 알고리즘 보다는 출력을 다뤄야하는 문제
# print 를 한다는 것은 굉장히 연산이 오래걸리는것
# 그러므로 print 를 줄여야 함
# 고로 리스트에 모든 출력을 담고 한번에 출력

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
res = []
for test_case in range(1, q+1):
    A, B ,C, D = map(int, input().split())
    res.append('#')
    res.append(test_case)
    ALICE = A/B
    BOB = C/D

    if ALICE > BOB:
        res.append('ALICE')
    elif ALICE < BOB:
        res.append('BOB')
    elif ALICE == BOB:
        res.append('DRAW')

str_res = str(res)
str_res = str_res.replace("['", '')
str_res = str_res.replace("']", '')
str_res = str_res.replace("', ", '')
str_res = str_res.replace(", '", ' ')
str_res = str_res.replace("'", '\n')

print(str_res)