import sys

L_stack = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
R_stack = []

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command[0] == 'L' and L_stack:
        R_stack.append(L_stack.pop())
    elif command[0] == 'D' and R_stack:
        L_stack.append(R_stack.pop())
    elif command[0] == 'B' and L_stack:
        L_stack.pop()
    elif command[0] == 'P':
        L_stack.append(command[2])

R_stack.reverse()
print(''.join(L_stack+R_stack))

# print(''.join(s))