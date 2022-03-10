from collections import deque

# 입력 받기
N, M = map(int, input().split())

# 초기 게임판 세팅
arr = [0] * 101
for i in range(101):
    arr[i] = i

hints = []
for _ in range(0, N + M):
    a, b = map(int, input().split())
    arr[a] = b

visited = [0] * 101
q = deque()
res = 0
q.append([1, res])
visited[1] = 1
while q:
    idx, res = q.popleft()
    #print("q", idx, res)
    if idx >= 100:
        break

    for dice in range(1, 7):
        if idx + dice <= 100:
            temp = arr[idx + dice]
            if visited[temp] == 0:
                #print("B", temp)
                visited[temp] = 1
                q.append([temp, res+1])

print(res)

