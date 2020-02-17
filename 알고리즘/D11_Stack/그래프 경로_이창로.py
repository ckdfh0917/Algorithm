import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    V, E = map(int, input().split())    # V : 노드의 갯수, E : 간선 정보

    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    arr[0] = [2 for _ in range(V+1)]
    for i in range(V+1):
        arr[i][0] = 2

    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1

    m, n = map(int, input().split())
    stack = []
    top = -1
    while True:

        flag = False
        # 찾아서 스택에 쌓기
        for i in range(1,V+1):
            if arr[m][i] == 1:
                if i == n:
                    flag = True
                    break
                arr[m][i] = 0
                stack.append(i)
                top += 1
        if flag:
            result = 1
            break
        # 팝해서 이동하기
        if top == -1:
            result = 0
            break
        else:
            m = stack.pop()
            top -= 1

    print('#{} {}' .format(test_case,result))
