munja = input()

for i in range(len(munja)):
    if munja[i] == 'C':
        print('Z', end='')
    elif munja[i] == 'B':
        print('Y', end='')
    elif munja[i] == 'A':
        print('X', end='')
    else:
        asc = ord(munja[i])
        t = asc - 3
        print(chr(t), end='')