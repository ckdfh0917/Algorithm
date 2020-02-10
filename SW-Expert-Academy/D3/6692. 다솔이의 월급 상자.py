import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    num = int(input())


    result = float(0)
    for i in range(num):
        p, money = map(float,input().split())
        #money = int(input())

        result += p * money

    print('#{} {}' .format(test_case,result))