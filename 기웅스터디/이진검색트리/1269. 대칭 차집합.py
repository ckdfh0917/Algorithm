N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def binary_search(start, end, target, arr):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return 0

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 1


A.sort()
B.sort()
cnt = 0
for a in A:
    cnt += binary_search(0, len(B)-1, a, B)

for b in B:
    cnt += binary_search(0, len(A)-1, b, A)

print(cnt)

