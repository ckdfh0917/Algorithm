import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    munja = input()

    stack = []
    top = -1
    cnt = 0
    stack.append(munja[0])
    for i in range(1,len(munja)):
        if len(stack) != 0:
            if stack[len(stack)-1] == munja[i]:
                stack.pop()
                top -= 1
                cnt += 2
            else:
                stack.append(munja[i])
                top += 1
        else:
            stack.append(munja[i])
            top += 1
    print('#{} {}'.format(test_case,len(munja) - cnt))