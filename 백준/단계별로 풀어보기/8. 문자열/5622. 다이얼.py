munja = input()

alpabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
arr = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
cnt = 0
for i in range(len(munja)):
    for j in range(len(alpabet)):
        if munja[i] == alpabet[j]:
            cnt += arr[j] + 1
print(cnt)
