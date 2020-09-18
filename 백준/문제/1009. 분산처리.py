import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    k = b % 4
    if k == 0:
        k = 4
    a **= k
    a = a % 10
    if a == 0:
        print(10)
    else:
        print(a)


'''
3 9 27 81 3 9

6 6 6 
7 9 3 1 
'''