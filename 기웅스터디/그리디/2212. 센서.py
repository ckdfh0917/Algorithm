N = int(input())
K = int(input())
lst = list(map(int, input().split()))

lst.sort()

arr = []
for i in range(N-1):
    arr.append(lst[i+1]-lst[i])

arr.sort()
# print(arr)
for _ in range(K-1):
    if arr:
        arr.pop()
    else:
        break
print(sum(arr))