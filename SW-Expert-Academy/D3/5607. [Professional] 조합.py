import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N, R = map(int,input().split())

    son = 1
    for i in range(N,N-R,-1):
        son *= i

    mother = 1
    for i in range(1,R+1):
        mother *= i
    K = son // mother
    result = K % 1234567891
    print('#{} {}'.format(test_case,result))
