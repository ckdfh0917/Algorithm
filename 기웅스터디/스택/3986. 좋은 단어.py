T = int(input())
cnt = 0
for test_case in range(T):
    s = input()
    # print(s)
    if len(s) % 2 == 1:
        continue
    stack = []
    flag = 0
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

    if not stack:
        cnt += 1
    # print(cnt)
print(cnt)