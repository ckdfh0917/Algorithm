n = int(input())

a = ''
b = ''

for j in range(n):
    if j % 2 == 1:
        a += ' ' + '*'
    else:
        b += '*' + ' '

for i in range(n):
    print(b)
    print(a)