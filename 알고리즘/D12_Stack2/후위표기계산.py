'''
6528-*2/+
-9.0
'''
postfix = list(input())

stack = []
k = 0
for i in range(len(postfix)):
    if 48 <= ord(postfix[i]) <= 57:
        stack.append(postfix[i])
    else:
        b = stack.pop()
        a = stack.pop()
        if postfix[i] == '+':
            temp = int(a) + int(b)
            stack.append(temp)
        elif postfix[i] == '-':
            temp = int(a) - int(b)
            stack.append(temp)
        elif postfix[i] == '*':
            temp = int(a) * int(b)
            stack.append(temp)
        elif postfix[i] == '/':
            temp = int(a) / int(b)
            stack.append(temp)
result = stack.pop()
print(result)

