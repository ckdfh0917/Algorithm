import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    temp = input()
    if len(temp) > 6:
        num = int(temp[5:-1])
        cmd = temp[0:3]
        # print(cmd, num)
    else:
        cmd = temp[0:3]

    if cmd == 'pus':
        queue.append(num)
    elif cmd == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd == 'siz':
        print(len(queue))
    elif cmd == 'emp':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'fro':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'bac':
        if queue:
            print(queue[-1])
        else:
            print(-1)
