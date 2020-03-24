N, M = map(int, input().split())
numbers = list(map(int, input().split()))

a = [0] * N
for i in range(M):
    a[numbers[i] - 1] = i+1
d = 1
cnt = 0
while d <= M:
    for i in range(N):
        flag = 0
        if a[i] == d:
            while True:
                if a[0] == d:
                    a.pop(0)
                    flag = 1
                    break
                if i+1 <= (len(a)//2)+1:
                    t = a.pop(0)
                    a.append(t)
                    cnt += 1
                else:
                    t = a.pop()
                    a.insert(0, t)
                    cnt += 1
        if flag == 1:
            d += 1
            break
print(cnt)