import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
# q = 1
dp = [[[[[False] * 2 for _ in range(20)] for _ in range(20)] for _ in range(20)] for _ in range(20)]

def find(k,a,b,c,d,str):
    print(result)
    if a == 0 and b == 0 and c == 0 and d == 0:
        return True
    if dp[k][a][b][c][d] == False:
        return False
    if k == 0:      # 마지막 자리가 0 이면
        if a > 0:   # 00 이면
            if find('0',a-1,b,c,d,result+'0'):
                return True
        if b > 0:   # 01 이면
            if find('1',a,b-1,c,d,result+'1'):
                return True
    else:           # 마지막 자리가 1 이면
        if c > 0:   # 10 이면
            if find('0',a,b,c-1,d,result+'0'):
                return True
        if d > 0:   # 11 이면
            if find('1',a,b,c,d-1,result+'1'):
                return True
    dp[k][a][b][c][d] = False

    return False


for test_case in range(1,q+1):
    A,B,C,D = map(int, input().split())
    print('#{} '.format(test_case), end='')
    result = ''
    if find(0,A,B,C,D,result+'0'):
        continue
    if find(1,A,B,C,D,result+'1'):
        continue
    print(result)
    print('impossible')
