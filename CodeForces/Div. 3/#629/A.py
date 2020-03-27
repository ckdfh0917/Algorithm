t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a >= b:
        if a % b == 0:
            print(0)
        else:
            t = a // b
            z = b * (t+1)
            print(z-a)
    else:
        print(b-a)