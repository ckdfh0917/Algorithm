import heapq
import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if not numbers:
            print(0)
        else:
            print(heapq.heappop(numbers)[1])
    else:
        heapq.heappush(numbers, (-num, num))
