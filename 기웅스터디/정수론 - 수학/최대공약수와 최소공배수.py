a, b = map(int, input().split())

def gcd(a, b):
    # print('k',a)
    if b == 0:
        return a
    else:
        res = gcd(b, a%b)
    return res

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcd(a,b):
    return a * b // gcd(a,b)

print(gcd(a,b))
print(lcd(a,b))