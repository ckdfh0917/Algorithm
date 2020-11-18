import sys

n = int(input())
arr = list(sys.stdin.readline().rstrip())
number = []
for i in range(n):
    number.append(int(input()))
alphabet = [chr(i+65) for i in range(26)]

# for i in range(len(arr)): # 배열에 대해서
#     if arr[i] in alphabet:
#         arr[i] = number[ord(arr[i]) - 65]
# print(arr)
stack = []
for i in range(len(arr)):
    if arr[i] == '+':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1+temp2)
    elif arr[i] == '-':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 - temp2)
    elif arr[i] == '*':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 * temp2)
    elif arr[i] == '/':
        temp2 = stack.pop()
        temp1 = stack.pop()
        stack.append(temp1 / temp2)
    else:
        stack.append(number[ord(arr[i]) - 65])

print("{0:.2f}".format(stack[0]))