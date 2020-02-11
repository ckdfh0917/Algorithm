# 테스트 케이스가 워낙 많아서 출력을 여러번 하면 안되고
# 답을 하나에 몰아서 출력 한번만 해준다

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def f(n):
    n_len = len(n)
    temp = 0
    for i in range(n_len):
        temp += int(n[i])
    if 0 < temp < 10:
        return str(temp)
    temp = str(temp)
    return f(temp)

result = []
for test_case in range(1,q+1):
    n = input()
    result += '#' + str(test_case) + ' ' + f(n)+ '\n'
print(''.join(result))
