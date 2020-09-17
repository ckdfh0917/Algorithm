import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    temp = a
    for i in range(b-1):
        temp *= a
        temp = temp % 10
    if temp == 10:
        print(temp)
    else:
        temp = temp % 10
        print(temp)


'''
3 9 27 81 3 9

6 6 6 
7 9 3 1 
'''