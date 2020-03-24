N, P = map(int, input().split())


s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []

cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    # print('a', a, b)
    if a == 1:
        if not s1:
            s1.append(b)
            cnt += 1
            # print('c',s1, s2, cnt)
        else:
            flag1 = 0
            while s1:
                flag1 = 0
                if b < s1[-1]:
                    s1.pop()
                    cnt += 1
                    flag1 = 1
                    # print('a',s1, s2, cnt)
                elif b == s1[-1]:
                    break
                else:
                    flag1 = 1
                    break
            if flag1 == 1:
                s1.append(b)
                cnt += 1
                # print('b',s1, s2, cnt)
    elif a == 2:
        if not s2:
            s2.append(b)
            cnt += 1
            # print(s1, s2)
        else:
            flag2 = 0
            while s2:
                flag2 = 0
                if b < s2[-1]:
                    s2.pop()
                    cnt += 1
                    flag2 = 1
                    # print(s1, s2)
                elif b == s2[-1]:
                    break
                else:
                    flag2 = 1
                    break

            if flag2 == 1:
                s2.append(b)
                cnt += 1
                # print(s1, s2)
    elif a == 3:
        if not s3:
            s3.append(b)
            cnt += 1
        else:
            flag3 = 0
            while s3:
                flag3 = 0
                if b < s3[-1]:
                    s3.pop()
                    cnt += 1
                    flag3 = 1
                elif b == s3[-1]:
                    break
                else:
                    flag3 = 1
                    break

            if flag3 == 1:
                s3.append(b)
                cnt += 1
    elif a == 4:
        if not s4:
            s4.append(b)
            cnt += 1
        else:
            flag4 = 0
            while s4:
                flag4 = 0
                if b < s4[-1]:
                    s4.pop()
                    cnt += 1
                    flag4 = 1
                elif b == s4[-1]:
                    break
                else:
                    flag4 = 1
                    break

            if flag4 == 1:
                s4.append(b)
                cnt += 1
    elif a == 5:
        if not s5:
            s5.append(b)
            cnt += 1
        else:
            flag5 = 0
            while s5:
                flag5 = 0
                if b < s5[-1]:
                    s5.pop()
                    cnt += 1
                    flag5 = 1
                elif b == s5[-1]:
                    break
                else:
                    flag5 = 1
                    break

            if flag5 == 1:
                s5.append(b)
                cnt += 1
    elif a == 6:
        if not s6:
            s6.append(b)
            cnt += 1
        else:
            flag6 = 0
            while s6:
                flag6 = 0
                if b < s6[-1]:
                    s6.pop()
                    cnt += 1
                    flag6 = 1
                elif b == s6[-1]:
                    break
                else:
                    flag6 = 1
                    break

            if flag6 == 1:
                s6.append(b)
                cnt += 1
print(cnt)