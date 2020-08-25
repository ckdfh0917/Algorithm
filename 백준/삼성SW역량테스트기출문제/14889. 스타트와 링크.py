N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N

start = [0]
res = 123457890
def find(index, cnt):
    global res
    if cnt == N // 2:
        link = []
        for i in range(1, N):
            if i not in start:
                link.append(i)
        sumS = 0
        sumL = 0
        for i in range(len(start)):
            for j in range(i+1, len(start)):
                sumS += arr[start[i]][start[j]] + arr[start[j]][start[i]]
        for i in range(len(link)):
            for j in range(i+1, len(link)):
                sumL += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        res = min(res, abs(sumL - sumS))
        return

    for i in range(index, N):
        if visited[i] == 0:
            visited[i] = 1
            start.append(i)
            find(i+1, cnt+1)
            visited[i] = 0
            start.pop()

find(1, 1)
print(res)