'''
DP
1. 가방의 크기가 i일 때 j번째 물건을 담을 수 있다면 j번째 물건을 담는 경우와 아닌 경우 중 최대값으로 채운다.

     d[i][j] = max(d[i][j-1],d[i-v[j]][j-1]+c[j])



2. 가방의 크기가 i일 때 j번째 물건을 담을 수 없다면 j-1번째 물건까지 담을 수 있는 최대 가치로 채운다.

     d[i][j] = d[i][j-1]

https://henry121407.tistory.com/106

좀 더 이해를 해봐야겠다
'''

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N, K = map(int, input().split())    # N: 물건의 갯수 K: 가방의 부피

    box = []
    V = [0]
    C = [0]
    for _ in range(N):
        a, b = map(int, input().split())
        V.append(a)
        C.append(b)

    d = [[0] * (N+1) for _ in range(K+1)]
    # print(V)
    # print(C)
    for i in range(1,K+1):      # 가방의 크기
        for j in range(1,N+1):  # 물건의 갯수
            #print('ㅊ',i,j,V[j])
            if i >= V[j]:       # 가방의 크기가 물건들의 부피보다 크거나 같으면
                #print('a',d[i][j-1], d[i-V[j]][j-1] + C[j])
                d[i][j] = max(d[i][j-1], d[i-V[j]][j-1] + C[j])     # 1. 가방의 크기가 i일 때 j번째 물건을 담을 수 있다면 j번째 물건을 담는 경우와 아닌 경우 중 최대값으로 채운다.
                                                                    # d[i-V[j]][j-1] + C[j] : d[i-V[i]][j-1] -> 최대 가방 부피에서 현재 가방 부피를 뺏을때의 최대값
                                                                    #                         C[j] -> d[i-V[i]][j-1] -> 현재 물건의 가치를 위의 최대값과 더한다.
            else:
                #print('b',d[i][j-1])
                d[i][j] = d[i][j-1]     # 2. 가방의 크기가 i일 때 j번째 물건을 담을 수 없다면 j-1번째 물건까지 담을 수 있는 최대 가치로 채운다.
            #print('d',d)
    # print(d[K][N])
    print('#{} {}' .format(test_case, d[K][N]))