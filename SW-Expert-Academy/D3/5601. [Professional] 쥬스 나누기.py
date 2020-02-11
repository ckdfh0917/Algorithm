# 함정은 없었음
# 그냥 N빵한 것

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N = int(input())
    print('#{} '.format(test_case), end='')
    for i in range(N):
        print('1/{}' .format(N), end=' ')
    print()