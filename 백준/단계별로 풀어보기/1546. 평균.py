N = int(input())
a = list(map(int,input().split()))
max_V = max(a)
num = 0
for i in a:
    num += i / max_V * 100
num = num / N
print(num)