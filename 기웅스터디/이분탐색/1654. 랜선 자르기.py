K, N = map(int, input().split())
lst = []
for i in range(K):
    lst.append(int(input()))


def find(min_V, max_V):
    global result
    mid = (min_V + max_V) // 2
    cnt = 0
    for i in range(K):
        if lst[i] >= mid:
           cnt += lst[i] // mid

    if min_V > max_V:
        return
    # print(min_V, mid, max_V)
    if cnt >= N:
        if result < mid:
           result = mid
        find(mid+1, max_V)
    else:
        find(min_V, mid-1)

result = 0
find(1, 2**31-1)
print(result)

