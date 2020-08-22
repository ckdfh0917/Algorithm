A, B = map(str, input().split())
A = A[::-1]
B = B[::-1]
if A > B:
    res = A
else:
    res = B
print(res)