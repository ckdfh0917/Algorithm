N = int(input())

lst = []

for _ in range(N):
    lst.append(input().split())
# print(lst)

lst.sort(key=lambda x:(int(x[0])))

# print(lst)
for x in lst:
    print(' '.join(x))