import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
#
dp = [[[[[True] * 21 for _ in range(21)] for _ in range(21)] for _ in range(21)] for _ in range(2)]
# dp[0][a][b][c][d]: 이전 0 이고, 00 a개 01 b개 10 c개 11 d개 있을 때 방문해봤으면 false
# dp[1][a][b][c][d]: 이전 1 이고, 00 a개 01 b개 10 c개 11 d개 있을 때 방문해봤으면 false


def find(a,b,c,d,str):
    # print(str)
    past = int(str[-1])
    # print(past)
    if a == 0 and b == 0 and c == 0 and d == 0:     # a, b, c, d를 조건에 맞게 다 쓰면
        print(str)
        return True
    if dp[past][a][b][c][d] == False:       # DP -> 이미 실패한 곳은 다시 가지 않는다다
        return False

    if past == 0:               # 마지막 자리가 0 이면
        if a > 0:               # 00 이면
            if find(a-1,b,c,d,str+'0'):
                return True
        if b > 0:               # 01 이면
            if find(a,b-1,c,d,str+'1'):
                return True
    else:                       # 마지막 자리가 1 이면
        if c > 0:               # 10 이면
            if find(a,b,c-1,d,str+'0'):
                return True
        if d > 0:               # 11 이면
            if find(a,b,c,d-1,str+'1'):
                return True
    # 재귀를 돌다가 조건에 맞는 abcd가 없다면 False
    dp[past][a][b][c][d] = False

    return False


for test_case in range(1,q+1):
    A,B,C,D = map(int, input().split())
    print('#{} '.format(test_case), end='')
    result = ''
    if find(A,B,C,D,'0'):
        continue
    if find(A,B,C,D,'1'):
        continue
    print('impossible')
