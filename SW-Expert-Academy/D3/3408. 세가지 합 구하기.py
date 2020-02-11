# for 문 돌리면 제한시간 초과됨
# for 문 없이도 충분히 S1,S2,S3를 구할 수 있음
# 혹시 몰라 한 리스트에 답을 묶어서 한번에 출력

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

result = []
for test_case in range(1,q+1):
    N = int(input())
    S1 = (N * (N+1)) // 2
    S2 = S1 * 2 - N
    S3 = S2 + N
    result += '#' + str(test_case) + ' ' + str(S1) + ' ' + str(S2) + ' ' + str(S3) + '\n'
print(''.join(result))