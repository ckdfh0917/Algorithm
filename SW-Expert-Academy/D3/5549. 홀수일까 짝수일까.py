import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    num = int(input())
    print('#{} '.format(test_case),end='')

    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')