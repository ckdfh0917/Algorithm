import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

maxV = 0
cnt = 0
sushi = []
visited = [0] * (d+1)
for i in range(N):
    t = int(input())
    sushi.append(t)
for i in range(k-1):
    sushi.append(sushi[i])

for i in range(N+k-1):
    if i >= k:
        visited[sushi[i-k]] -= 1
        if visited[sushi[i-k]] == 0:
            cnt -= 1
        if visited[sushi[i]] == 0:
            cnt += 1
        visited[sushi[i]] += 1
    else:
        if visited[sushi[i]] == 0:
            visited[sushi[i]] = 1
            cnt += 1
        else:
            visited[sushi[i]] += 1

    if visited[c] == 0:
        maxV = max(maxV, cnt + 1)
    else:
        maxV = max(maxV, cnt)


print(maxV)
