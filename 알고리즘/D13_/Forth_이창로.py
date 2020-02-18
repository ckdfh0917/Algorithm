import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    cal = list(input().split())

    num = []
    result = 0
    for i in cal:
        if i != '+' and i != '-' and i != '/' and i != '*' and i != '.':
            num.append(i)
        else:
            if len(num) >= 2:
                b = num.pop()
                b = int(b)
                a = num.pop()
                a = int(a)
                if i == '+':
                    temp = a + b
                    num.append(temp)
                elif i == '-':
                    temp = a - b
                    num.append(temp)
                elif i == '*':
                    temp = a * b
                    num.append(temp)
                elif i == '/':
                    temp = a / b
                    num.append(int(temp))
            else:
                if i == '.':
                    result = num.pop()
                    break
                else:
                    result = 'error'
                    break
    if num:
        result = 'error'
    print('#{} {}'.format(test_case,result))