import heapq
import sys
input = sys.stdin.readline

N = int(input())

pq = []

for _ in range(N):
    num = int(input())
    # print(num, pq)
    if num == 0:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, num)