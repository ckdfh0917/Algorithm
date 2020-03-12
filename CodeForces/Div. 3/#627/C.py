q = int(input())
for z in range(q):
    frog = ['0'] + list(input())
    print('#{}=================='.format(z))
    for d in range(1, len(frog)):
        k = d
        flag = 0
        print('aaa',d)
        while k > 0:
            print(k)
            if frog[k] == 'L':
                for i in range(k-1,-1,-1):
                    if frog[i] == 'L':
                        k = max(0, i - d)
                        break
                    else:
                        flag = 1
                        break
                if flag == 1:
                    print('====out====')
                    break
            elif frog[k] == 'R':
                stack = []
                for i in range(k+d,k,-1):
                    if frog[i] == 'R':
                        stack.append(i)
                
                #         k = min(len(frog), i + d)
                #         break
                # else:
                #     flag = 2
                #     break
                # if flag == 2:
                #     break
        if flag == 1:
            continue
        elif flag == 2:
            print(d)
            break
