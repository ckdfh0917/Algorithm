N = int(input())
munja = list(input())

stack = []
numbers = []

for _ in range(N):
    numbers.append(int(input()))

for i in range(len(munja)):
    if munja[i] == '*':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 * n1)
    elif munja[i] == '+':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 + n1)
    elif munja[i] == '-':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 - n1)
    elif munja[i] == '/':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 / n1)
    else:
        stack.append(numbers[ord(munja[i])-ord('A')])

res = stack.pop()
temp = '{0:.2f}'.format(res)
print(temp)
