import sys
input = sys.stdin.readline
A, B, V = map(int, input().split())


k = V - A
if k % (A-B) != 0:
    res = k // (A - B) + 2
else:
    res = k // (A - B) + 1


print(res)

# 100 90 101
# 44 43 100
# -> 57