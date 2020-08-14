t = int(input())

for q in range(t):
    n = int(input())
    a = list(map(int, input()))

    res = 0
    for i in range(n):
        for j in range(i, n):
            sumV = sum(a[i:j+1])
            if sumV == j - i + 1:
                res += 1
            
    print(res)