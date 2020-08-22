M, N = map(int, input().split())

def sosu(n):
    for i in range(2,n+1):
        if a[i] == 1:
            if M <= i:
                print(i)
            for j in range(i*2,n+1,i):
                a[j] = 0

a = [0] + [0] + [1] * (N-1)
sosu(N)
