a = list(input())

b = ['(', '[']
c = [')', ']']
stack = []
result = 0
flag = 0
temp = 1
for i in a:
    # print(i)
    if i in b:
        if flag == 2:
            # print(stack, temp)
            for j in stack:
                if j == '(':
                    temp *= 2
                elif j == '[':
                    temp *= 3
            result += temp
            # print('a',result)
        stack.append(i)
        temp = 1
        flag = 1
    else:
        if not stack:
            flag = 1
            break
        elif (i == ')' and stack[-1] == '[') or (i == ']' and stack[-1] == '('):
            # print(0)
            flag = 1
            break
        elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '['):
            if stack[-1] == '(':
                temp *= 2
            elif stack[-1] == '[':
                temp *= 3
            flag = 2
            stack.pop()
            # print(temp)


if stack:
    flag = 1
if flag == 1:
    print(0)
result += temp
if flag != 1:
    print(result)
