
def GetSubset():
    global cnt
    a = []
    for i in range(1<<N):
        b = []
        for j in range(N):
            temp = i & (1<<j)
            if temp:
                b.append(temp)
        x = sum(b)
        if x == K:
            cnt += 1
        a.append(b)

    print(a)

N = 10
K = 10
cnt = 0
GetSubset()
print(cnt)