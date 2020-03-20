a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

if a1 == a2:
    a4 = a3
elif a2 == a3:
    a4 = a1
elif a3 == a1:
    a4 = a2

if b1 == b2:
    b4 = b3
elif b2 == b3:
    b4 = b1
elif b3 == b1:
    b4 = b2

print(a4, b4)