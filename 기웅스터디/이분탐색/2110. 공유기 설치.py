n, c = map(int, input().split())

home = []
for _ in range(n):
    home.append(int(input()))
home.sort()
arr = [0] * (max(home) + 1)
for x in home:
    arr[x] = 1
print(arr)
installed = [0] * (max(home) + 1)
print(installed)

q = []
stack = []
result = 0
def f(a, i):
    global result
    print(a, i, stack)
    if len(stack) == c:
        temp = 1987654321
        for x in range(len(stack)-1):
            temp = min(temp, stack[x+1] - stack[x])
            result = max(temp, result)
        stack.pop()
        if i+1 > n:
            stack.pop()
            print('aaa')
            f(a, i)
        print('dddd')
        f(a, i)
    else:
        if a == len(home):
            stack.pop()
            print('bbbb')
            f(a, i)
        else:
            stack.append(home[a])
            print('cccc')
            f(a+1, i)



for i in range(n-c+1):
    print('xxx',i)
    f(i, i)
print(result)