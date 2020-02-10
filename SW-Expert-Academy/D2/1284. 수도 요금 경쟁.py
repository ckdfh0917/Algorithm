import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    P, Q, R, S, W = map(int, input().split())   # P : A사 1L당 요금
                                                # Q : R리터 이하 요금
                                                # R : 기본 요금의 리터양
                                                # S : B사 기본 사용량 초과 1L당 요금
                                                # W : 한달간 사용하는 수도의 양
    print('#{} ' .format(test_case), end='')
    #print(P, Q, R, S, W)

    A = 0
    B = 0

    A = P * W


    if W - R > 0:
        B = (W - R) * S + Q
    else:
        B = Q

    if A > B:
        print(B)
    else:
        print(A)