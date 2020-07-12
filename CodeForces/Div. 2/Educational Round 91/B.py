T = int(input())

def per():
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if p[i] < p[j] and p[j] > p[k]:
                    return [i+1, j+1, k+1]

    return -1

for _ in range(T):
    n = int(input())
    p = list(map(int, input().split()))


    lst = per()
    if lst == -1:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, lst)))
