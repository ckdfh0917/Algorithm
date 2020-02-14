# D10_Stack의 memoization.py에서 DP 를 사용함
# 재귀는 999번이 최대임
# 아예 memo 리스트에 입력 제한 값 다 때려넣고 시작해야함

import sys
sys.stdin = open('input.txt', 'r')

memo = [0,1]
def f(n):
    for i in range(2,10**6+1):
        memo.append(memo[i-1] + 2*i - 1)
        #print(memo)
    return memo[n-1]

f(10**6+1)
q = int(input())

for test_case in range(1,q+1):
    A, B = map(int, input().split())

    n = A//B
    print('#{} {}'.format(test_case,memo[n]))