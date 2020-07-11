N = int(input())
k = int(input())

low = 1
high = k
res = -1

while low <= high:
    cnt = 0
    mid = (low+high) // 2

    for i in range(1, N+1):
        cnt += min(mid // i, N)

    if cnt < k:
        low = mid + 1
    else:
        res = mid
        high = mid - 1

print(res)
