import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    lst = []
    n = int(input())
    for i in range(n):
        lst.append(list(map(int, input().split())))

    # for i in range(n):
    #     print(lst[i])
    visited =[[0] * n for _ in range(n)]
    stack = []
    for i in range(n):
        for j in range(n):
            if lst[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                k = j
                while True:

                    if (lst[i][k+1] != 0 and lst[i][k+2] == 0):
                        stack.append([i,j+1])
                    if lst[i+1][j] != 0:
                        stack.append([i+1,j])