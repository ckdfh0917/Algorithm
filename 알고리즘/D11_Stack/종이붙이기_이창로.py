import sys
sys.stdin = open('input.txt', 'r')

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return f(n-2)*2 + f(n-1)



q = int(input())
# 전에꺼 더하기 전전에꺼 곱하기2 한후 더하기
for test_case in range(1,q+1):
    N = int(input())

    num = N // 10

    result = f(num)

    print('#{} {}'.format(test_case,result))