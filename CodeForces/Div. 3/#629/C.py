t = int(input())
for k in range(t):
    n = int(input())
    x = input()
    # print(x)

    if len(x) == 1:
        a = 1
        b = 1
    else:
        if x[1] == '2':
            a = '11'
            b = '11'
        elif x[1] == '1':
            a = '11'
            b = '10'
        elif x[2] == '0':
            a = '10'
            b = '10'

        for i in range(1,len(x)-1):
            # 22222222
            if x[i-1] == '2' and x[i] == '2':
                a += '1'
                b += '1'
            elif x[i-1] == '2' and x[i] == '1':
                if a[-1] == '1' and b[-1] == '1':
                    a += '1'
                    b += '0'
                elif a[-1] == '2' and b[-1] == '0':
                    a += '0'
                    b += '1'
                elif a[-1] == '0' and b[-1] == '2':
                    a += '0'
                    b += '1'
            elif x[i-1] == '2' and x[i] == '0':
                if a[-1] == '1' and b[-1] == '1':
                    a += '0'
                    b += '0'
                elif a[-1] == '1' and b[-1] == '0':
                    a += '1'
                    b += '1'
                elif a[-1] == '0' and b[-1] == '1':
                    a += '1'
                    b += '1'
            # 11111111111
            elif x[i-1] == '1' and x[i] == '2':
                if a[-1] == '1' and b[-1] == '0':
                    a += '0'
                    b += '2'
            elif x[i-1] == '1' and x[i] == '1':
                if a[-1] == '1' and b[-1] == '0':
                    a += '0'
                    b += '1'
                elif a[-1] == '0' and b[-1] == '0':
                    a += '2'
                    b += '2'
                elif a[-1] == '0' and b[-1] == '1':
                    a += '0'
                    b += '1'
            elif x[i-1] == '1' and x[i] == '0':
                if a[-1] == '1' and b[-1] == '0':
                    a += '0'
                    b += '0'
                elif a[-1] == '0' and b[-1] == '1':
                    a += '0'
                    b += '0'
                elif a[-1] == '0' and b[-1] == '0':
                    a += '2'
                    b += '2'

            # 0000000000
            elif x[i-1] == '0' and x[i] == '2':
                if a[-1] == '0' and b[-1] == '0':
                    a += '1'
                    b += '1'
            elif x[i-1] == '0' and x[i] == '1':
                if a[-1] == '0' and b[-1] == '0':
                    a += '1'
                    b += '0'
            elif x[i-1] == '0' and x[i] == '0':
                if a[-1] == '0' and b[-1] == '0':
                    a += '0'
                    b += '0'
    print(a)
    print(b)