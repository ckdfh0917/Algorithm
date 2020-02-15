import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1,11):
    N, num = map(str, input().split())
    N = int(N)
    stack = []
    i = 0
    while i < N:
        flag = 0
        if stack and stack[-1] == str(num[i]):
            stack.pop()
            flag = 1
        if flag != 1:
            stack.append(str(num[i]))
        i += 1
    print('#{} {}'.format(test_case,''.join(map(str,stack))))