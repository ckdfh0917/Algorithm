N = int(input())
arr = list(map(int, input().split()))
box = [1] * len(arr)
res = 0

for i in range(0, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            box[i] = max(box[i], box[j] + 1)
    res = max(res, box[i])

print(res)
