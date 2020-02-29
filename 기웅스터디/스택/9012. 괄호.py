N = int(input())

for i in range(N):
    p = input()
    stack = []
    # print(i+1)
    flag = 0
    for i in p:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                print('NO')
                flag = 1
                break
            else:
                stack.pop()
    if not stack and flag == 0:
        print('YES')
    elif flag == 0:
        print('NO')