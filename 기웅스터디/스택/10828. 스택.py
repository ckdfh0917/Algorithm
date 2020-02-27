import sys
input = sys.stdin.readline
N = int(input())

stack = []
for _ in range(N):
    temp = input()
    # print(temp)
    cmd = ''
    num = 0
    if len(temp) > 6:
        num = int(temp[5:-1])
        cmd = temp[0:3]
        # print(cmd, num)
    else:
        cmd = temp[0:3]

    if cmd == 'pus':
        stack.append(num)
    elif cmd == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
    elif cmd == 'siz':
        print(len(stack))
    elif cmd == 'emp':
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    # print('s',stack)