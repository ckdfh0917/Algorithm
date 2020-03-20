n = int(input())

arr = [1] * n
temp = 0
for i in range(1,n):
    arr[i] = arr[i-1] + i
    if arr[i] > n:
        temp = i
        break
# print(temp)
# print(arr)
adj = []
for i in range(1,temp+1):
    if i % 2 == 0:
        adj.append([1, i])
    else:
        adj.append([i, 1])
# print(adj)

k = n - arr[temp-1]
# print(k)
if temp % 2 == 0:
    x, y = adj[temp-1]
    x += k
    y -= k
    x = str(x)
    y = str(y)
    print(x + '/' + y)
else:
    x, y = adj[temp - 1]
    x -= k
    y += k
    x = str(x)
    y = str(y)
    print(x + '/' + y)