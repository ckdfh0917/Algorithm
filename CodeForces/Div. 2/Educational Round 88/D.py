n = int(input())
a = list(map(int, input().split()))


maxV = 0
for i in range(n):
    for j in range(i, n):
        lst = a[i:j+1]
        # print('a',lst)
        lst.pop(lst.index(max(lst)))
        # print('b',lst)
        # print('c',sum(lst))
        maxV = max(maxV, sum(lst))
print(maxV)