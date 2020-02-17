q = int(input())

for test_case in range(1, q+1):
    munja = list(input())

    s = []
    result = 1
    for i in range(len(munja)):
        if munja[i] == '[' or munja[i] == '{' or munja[i] == '(':
            s.append(munja[i])
        elif munja[i] == ']' or munja[i] == '}' or munja[i] == ')':
            if len(s) != 0:
                temp = s.pop()
                #print(temp, munja[i])
                if temp == '[' and munja[i] == ']':
                    pass
                elif temp == '{' and munja[i] == '}':
                    pass
                elif temp == '(' and munja[i] == ')':
                    pass
                else:
                    result = 0
                    break
            else:
                result  = 0
                break
    if len(s) != 0:
        result = 0
    print('#{} {}' .format(test_case,result))
