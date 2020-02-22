N = int(input())
cnt = 0
for _ in range(N):
    arr = [0] * 26
    munja = input()
    flag = 0
    for i in range(len(munja)):
        if i+1 < len(munja) and munja[i] == munja[i+1]:
            continue
        else:
            k = ord(munja[i]) - 97
            if arr[k] == 0:
                arr[k] = 1
            else:
                flag = 1
                break
    if flag == 0:
        cnt += 1
print(cnt)