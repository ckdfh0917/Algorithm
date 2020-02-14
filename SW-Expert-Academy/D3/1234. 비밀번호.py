import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1,11):
    N, num = map(int, input().split())

    num = str(num)
    stack = []
    i = 0
    while i < N-1:
        flag = 0
        if stack and stack[-1] == str(num[i]):
            stack.pop()
            flag = 1
        if flag != 1:
            stack.append(str(num[i]))
        print(stack)
        i += 1
    print(stack)