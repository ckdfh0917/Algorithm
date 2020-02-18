import sys
sys.stdin = open('input.txt', 'r')

# 피연산자인지 확인 ( 숫자인지)
def is_number(x):
    if 48 <= ord(x) <= 57:
        return x


def isp(token):  # isp : 스택의 top연산자 우선순위
    if token == '(':
        return 0
    elif token == '+' or token == '-':
        return 1
    elif token == '*' or token == '/':
        return 2


def icp(token):  # icp : 스택으로 들어갈 연산자 우선순위
    if token == '(':
        return 3
    elif token == '+' or token == '-':
        return 1
    elif token == '*' or token == '/':
        return 2

for test_case in range(1,11):
    N = int(input())
    infix = list(input())  # 입력받기
    postfix = []  # 변환결과 저장
    stack = []  # 스택

    for x in infix:
        # print(x)
        if is_number(x):
            postfix.append(x)
        else:

            if x == '(':
                stack.append(x)
            elif x == ')':
                while True:
                    temp = stack.pop()
                    if temp == '(':
                        break
                    postfix.append(temp)

            elif icp(x) > isp(stack[-1]):
                if icp(x) == isp(stack[-1]):
                    temp = stack.pop()
                    postfix.append(temp)
                    stack.append(x)
                else:
                    stack.append(x)
            elif icp(x) <= isp(stack[-1]):
                temp = stack.pop()
                postfix.append(temp)
                stack.append(x)

    # 중위-> 후위 변환 연산 : 교재 참고하면서 작성
    # for c in postfix:
    #     print(c, end="")


    stack2 = []
    k = 0
    for i in range(len(postfix)):
        if 48 <= ord(postfix[i]) <= 57:
            stack2.append(postfix[i])
        else:
            b = stack2.pop()
            a = stack2.pop()
            if postfix[i] == '+':
                temp = int(a) + int(b)
                stack2.append(temp)
            elif postfix[i] == '-':
                temp = int(a) - int(b)
                stack2.append(temp)
            elif postfix[i] == '*':
                temp = int(a) * int(b)
                stack2.append(temp)
            elif postfix[i] == '/':
                temp = int(a) / int(b)
                stack2.append(temp)
    result = stack2.pop()
    print('#{} {}'.format(test_case,result))

