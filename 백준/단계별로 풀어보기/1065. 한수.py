X = int(input())

if X >= 100:
    cnt = 99
    for i in range(100,X+1):
        X = str(i)
        diff = int(X[0]) - int(X[1])
        if int(X[1]) - int(X[2]) == diff:
            # print(X)
            cnt += 1
elif X < 100:
    cnt = X
print(cnt)