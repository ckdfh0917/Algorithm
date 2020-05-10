def find(n, lst):
    # print('lll',n, lst)
    while len(n) > 1:
        for j in range(3):
            i = 0
            while i < len(n):
                if lst[j] == n[i]:
                    print('aa', n)
                    b = n.pop(i + 1)
                    cal = n.pop(i)
                    a = n.pop(i - 1)
                    if cal == '+':
                        res = a + b
                    elif cal == '-':
                        res = a - b
                    elif cal == '*':
                        res = a * b
                    n.insert(i - 1, res)
                    continue
                i += 1
    return n


def solution(expression):
    answer = 0

    # print(expression)
    numbers = []
    temp = 0
    stack = []
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            numbers.append(int(expression[temp:i]))
            temp = i + 1
            numbers.append(expression[i])
    numbers.append(int(expression[temp:]))
    # print(numbers)

    order = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    for i in range(6):
        nums = numbers[:]
        result = find(nums, order[i])
        print('rr', result)
        result = abs(result[0])
        answer = max(answer, result)

    return answer