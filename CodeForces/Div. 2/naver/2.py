# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
S = 'ACCAABBC'
# S ='ABCBBCBA'
# S = 'BABABA'
def solution(S):
    # write your code in Python 3.6
    stack = []
    for i in range(len(S)):
        if not stack:
            stack.append(S[i])
        else:
            if stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
    ans = ''.join(stack)
    return ans

print(solution(S))