munja = input()
arr = [-1] * 26
alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(munja)):
    flag = 0
    for j in range(len(alpabet)):
        if munja[i] == alpabet[j]:
            if arr[j] == -1:
                arr[j] = i
                break
print(' '.join(map(str, arr)))