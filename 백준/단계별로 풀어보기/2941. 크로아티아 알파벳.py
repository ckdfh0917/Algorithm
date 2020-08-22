c_alpabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

munja = input()
n = len(munja)
munja = munja +'00'

i = 0
cnt = 0
while i < n:
    if munja[i:i+2] in c_alpabet:
        cnt += 1
        i += 2
    elif munja[i:i+3] in c_alpabet:
        cnt += 1
        i += 3
    elif munja[i] not in c_alpabet:
        cnt += 1
        i += 1
print(cnt)