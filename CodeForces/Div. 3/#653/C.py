t = int(input())

for _ in range(t):
    n = int(input())
    bracket = list(input())

    # print(bracket)
    stack = []

    cnt = 0
    for x in bracket:
        if x == ')':
            if not stack:
                cnt += 1
            else:
                stack.pop()
        else:
            stack.append(x)
    print(cnt)