N, d, k, c = map(int, input().split())

maxV = 0
cnt = 0
visited = [0] * (N+1)
for i in range(N):
    t = int(input())
    # print('a', cnt, sushi)
    if i >= k:
        flag =
        print(p)
        if p not in sushi:
            cnt -= 1
        if t not in sushi:
            cnt += 1
        sushi.append(t)
    else:
        if visited[t] == 0:
            visited[t] = 1
            cnt += 1
    if visited[c] == 0:
        maxV = max(maxV, cnt + 1)
    # print('b', cnt, sushi)
    maxV = max(maxV, cnt)


print(maxV)
