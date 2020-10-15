from collections import deque

N, K = map(int, input().split())
numbers = list(map(int, input().split()))


visited = set()
visited.add(str(numbers))

# print(visited)
q = deque()
q.append([numbers, 0])

ans = -1
sorted_num = sorted(numbers)

while q:
    now, cnt = q.popleft()

    if now == sorted_num:
        ans = cnt
        break

    for i in range(N-K+1):
        temp = now[:]
        sub_num = now[i:i+K]
        sub_num.reverse()

        for j in range(K):
            temp[i+j] = sub_num[j]

        if str(temp) not in visited:
            # print(str(temp))
            visited.add(str(temp))
            q.append([temp, cnt+1])

print(ans)

