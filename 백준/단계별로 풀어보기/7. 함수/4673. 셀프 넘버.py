def SelfNumber(n):
    if n > 10000:
        return
    elif 1 <= n < 10:
        pass

def Create(n):
    global arr
    if n > 10:
        return
    elif n >= 1000:
        a = n // 100
        b = n % 100
        c = b // 10
        d = b % 10
        e = a + c + d
        arr[e] = 1
        Create(e)
    elif n >= 10:
        a = n // 10
        b = n % 10
        c = n + a + b
        arr[c] = 1
        Create(c)
    else:
        a = n + n
        arr[n] = 1
        Create(a)

arr = [0] * 1001

Create(1)
print(arr)