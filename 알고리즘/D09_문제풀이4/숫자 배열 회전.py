import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def rot(list,n):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            temp[j][n-1-i] = list[i][j]
    return temp

for test_case in range(1, q+1):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    print('#{}'.format(test_case))

    aa = rot(arr,N)
    result = []
    for i in range(N):
        result.append(aa)
        aa = rot(aa,N)
    for j in range(N):
        for k in range(3):
            print(''.join(map(str,result[k][j])), end=' ')
        print()