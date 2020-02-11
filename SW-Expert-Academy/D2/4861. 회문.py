import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    N, M = map(int, input().split())
    print('#{} ' .format(test_case), end='')

    munja = []
    for i in range(N):
        munja.append(input())
    #print(munja)

    # 가로
    for i in range(N):
        for j in range(N):
            flag = 0
            for k in range(N//2):
                if j+k < N and 0 <= M+j-1-k < N:
                    if munja[i][j+k] != munja[i][M+j-1-k]:
                        flag = 0
                        break
                    else:
                        flag = 1
                else:
                    break
            if flag == 1:
                print(munja[i][j:j+M])
                break

    # 세로
    for i in range(N):
        for j in range(N):
            flag2 = 0
            for k in range(N//2):
                if j+k < N and 0 <= M+j-1-k < N:
                    if munja[j+k][i] != munja[M+j-1-k][i]:
                        flag2 = 0
                        break
                    else:
                        flag2 = 1
                else:
                    break
            if flag2 == 1:
                for l in range(j,j+M):
                    print(munja[l][i], end='')
                print()