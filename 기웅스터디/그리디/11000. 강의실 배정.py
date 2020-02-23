N = int(input())

lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)

# print(lst)
max_V = 0
for i in range(N):
    if max_V < lst[i][1]:
        max_V = lst[i][1]
# print(max_V)
arr = [0] * (max_V + 1)
for i in range(N):
    a, b = lst[i][0], lst[i][1]
    for k in range(a,b):
        arr[k] += 1

print(max(arr))

# res = []
# for i in range(N-1):
#     s1, e1 = lst[i][0], lst[i][1]
#     for j in range(i+1,N):
#         s2, e2 = lst[j][0], lst[j][1]
#         if e1 <= s2:
#             temp = lst[i]+lst[j]
#         else:

