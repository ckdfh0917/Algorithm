import heapq
N = int(input())

lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)

new_lst = sorted(lst, key=lambda x: (x[0], x[1]))
print(new_lst)

pq = []
heapq.heappush(pq, (lst[0][1], lst[0][0]))
for i in range(1, N):
    print(pq)
    if pq[-1][1] <= lst[i][0]:
        heapq.heappop(pq)
        heapq.heappush(pq, (lst[i][1], lst[i][0]))
    else:
        heapq.heappush(pq, (lst[i][1], lst[i][0]))

print(pq)
print(len(pq))