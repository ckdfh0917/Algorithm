import sys
input = sys.stdin.readline
N = int(input())

Q = [i for i in range(1,N+1)]
i = 0
n = N
while n > 1:
    if len(Q) % 2 == 0:
        Q = Q[1::2]
    else:
        temp = Q[-1]
        Q = Q[1::2]
        Q.insert(0,temp)
    n = len(Q)
    # print('a',Q)
print(Q[0])