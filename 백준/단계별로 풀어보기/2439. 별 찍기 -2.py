N = int(input())
for i in range(1,N+1):
    a = ['*'] * i
    b = [' '] * (N-i)
    c = b + a
    print(''.join(c))
