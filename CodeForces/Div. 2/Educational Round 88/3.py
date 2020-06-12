# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq

def solution(A):
    # write your code in Python 3.6
    p = []
    for i in range(len(A)):
        heapq.heappush(p, A[i])
    cnt = 0
    while len(p) > 1:
        t1 = heapq.heappop(p)
        t2 = heapq.heappop(p)
        temp = t1 + t2
        cnt += temp
        heapq.heappush(p, temp)

    return cnt

solution(A)