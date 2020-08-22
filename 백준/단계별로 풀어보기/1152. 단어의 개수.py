munja = input()

if len(munja) == 1 and munja[0] == ' ':
    print(0)
elif len(munja) != 0:
    cnt = 1
    for i in range(len(munja)):
        if munja[0] == ' ' and i == 0:
            continue
        if i == len(munja) -1 and munja[i] == ' ':
            break
        if munja[i] == ' ':
            cnt += 1
    print(cnt)
elif len(munja) == 0:
    print(0)