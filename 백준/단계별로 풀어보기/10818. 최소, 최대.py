N = int(input())
a = list(map(int,input().split()))
min_V = 1000000
max_V = -1000000
for i in a:
    if min_V > i:
        min_V = i
    if max_V < i:
        max_V = i
print(min_V,max_V)