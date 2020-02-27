import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(list(map(int, input().split())))
    print('#{} '.format(test_case), end='')

    # for i in range(n):
    #     print(lst[i])
    visited =[[0] * n for _ in range(n)]
    stack = []
    result = []
    for i in range(n):
        for j in range(n):
            if lst[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                a, b = i, j
                k = j
                while True:
                    visited[i][k] = 1
                    if k+1 < n:
                        if lst[i][k+1] != 0 and visited[i][k+1] == 0:
                            k += 1
                            continue
                        else:
                            break
                    else:
                        break
                temp_j = k
                k = i
                while True:
                    visited[k][j] = 1
                    if k+1 < n:
                        if lst[k+1][j] != 0 and visited[k+1][j] == 0:
                            k += 1
                            continue
                        else:
                            break
                    else:
                        break
                temp_i = k
                for x in range(a, temp_i+1):
                    for y in range(b, temp_j+1):
                        visited[x][y] = 1
                # print(a, b, temp_i, temp_j)
                result.append([temp_j+1 - b, temp_i+1 - a])

    # print(result)
    res = sorted(result, key=lambda x:(x[0]*x[1], x[1]))
    # print(res)
    print(len(res), end=' ')
    for i in range(len(res)):
        print(res[i][1],res[i][0], end=' ')
    print()