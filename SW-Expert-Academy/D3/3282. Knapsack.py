'''
1. 가방의 크기가 i일 때 j번째 물건을 담을 수 있다면 j번째 물건을 담는 경우와 아닌 경우 중 최대값으로 채운다.

     d[i][j] = max(d[i][j-1],d[i-v[j]][j-1]+c[j])



2. 가방의 크기가 i일 때 j번째 물건을 담을 수 없다면 j-1번째 물건까지 담을 수 있는 최대 가치로 채운다.

     d[i][j] = d[i][j-1]

https://henry121407.tistory.com/106
'''

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N, K = map(int, input().split())    # N: 물건의 갯수 K: 가방의 부피

    box = []
    V = []
    C = []
    for _ in range(N):
        a, b = map(int, input().split())
        V.append(a)
        C.append(b)

    d = [[0] * 1001 for _ in range(101)]

    for i in range(K):
        for j in range(N):
            if i >= V[j]:
                d[i][j] = max(d[i][j-1], d[i-V[j]][j-1] + C[j])
            else:
                d[i][j] = d[i][j-1]
    print(d[K][N])
    #print('#{} {}' .format(test_case, max_C))