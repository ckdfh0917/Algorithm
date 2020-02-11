# 처음 풍선을 터트릴 때 써진 숫자만큼 상하좌우의 꽃가루의 최대합을 구하는 문제

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
dx = [-1, 0, 1, 0]    # 위 오른 아래 왼
dy = [0, 1, 0, -1]

for test_case in range(1, q+1):
    N, M = map(int, input().split())
    print('#{} '.format(test_case), end='')
    balloon = []
    for _ in range(N):
        balloon.append(list(map(int, input().split())))

    pang = 0
    for i in range(N):
        for j in range(M):
            temp = balloon[i][j]
            for k in range(4):
                for l in range(1,balloon[i][j]+1):
                    if 0 <= i+dx[k]*l < N and 0 <= j+dy[k]*l < M:
                        temp += balloon[i+dx[k]*l][j+dy[k]*l]
            if pang < temp:
                pang = temp
    print(pang)