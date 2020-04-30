N, K = map(int, input().split())

num = list(map(int, input().split()))
plug = [0] * (max(num) + 1)
result = 0

for i in range(K):
    pluggedin = False

    for j in range(N):
        if plug[j] == num[i]:
            pluggedin = True
            break

    if pluggedin:
        continue

    for j in range(N):
        if plug[j] == 0:
            plug[j] = num[i]
            pluggedin = True
            break

    if pluggedin:
        continue

    idx = -1        # plug 위치
    deviceidx = -1  # 가장 안쓰는 용품
    for j in range(N):
        lastidx = 0
        for k in range(i, K):
            if plug[j] == num[k]:
                break
            lastidx += 1

        if lastidx > deviceidx:
            idx = j
            deviceidx = lastidx
    result += 1
    plug[idx] = num[i]
print(result)


