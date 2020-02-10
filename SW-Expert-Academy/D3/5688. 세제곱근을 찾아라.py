import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    num = int(input())
    print('#{} ' .format(test_case), end='')
    if num == 1:
        print(1)
    else:
        for i in range(1,num):
            #(num, i**3)
            result = -1
            if num > i**3:
                continue
            elif num == i**3:
                result = i
                break
            elif num < i**3:
                break
        print(result)