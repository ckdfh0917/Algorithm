def Create(n):
    global arr
    if n > 10000:
        return
    elif n >= 1000:
        a = n // 1000
        b = n % 1000
        c = b // 100
        d = b % 100
        e = d // 10
        f = d % 10
        g = n + a + c + e + f
        arr[g] = 1
    elif n >= 100:
        a = n // 100
        b = n % 100
        c = b // 10
        d = b % 10
        e = n + a + c + d
        arr[e] = 1
    elif n >= 10:
        a = n // 10
        b = n % 10
        c = n + a + b
        # print(n, c)
        arr[c] = 1
    else:
        a = n + n
        # print(n, a)
        arr[a] = 1

arr = [1] + [0] * 11000

for i in range(1,10000):
    Create(i)
# print(arr)

for i in range(1,10001):
    if arr[i] == 0:
        print(i)