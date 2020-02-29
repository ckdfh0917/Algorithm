'''
백트래킹을 이용한 DFS
'''
q = int(input())

def DFS(i, temp):

    global min_V, max_V
    # 끝까지 탐색
    if i == N:
        print(temp)
        min_V = min(min_V, temp)
        max_V = max(max_V, temp)
        return
    if op[0] > 0:
        op[0] -= 1
        DFS(i+1, temp + numbers[i])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        DFS(i+1, temp - numbers[i])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        DFS(i+1, temp * numbers[i])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if temp < 0:
            DFS(i+1, -(-temp // numbers[i]))
        else:
            DFS(i+1, temp // numbers[i])
        op[3] += 1


for test_case in range(1, q+1):
    N = int(input())
    op = list(map(int, input().split()))     # +,-,*,/
    numbers = list(map(int, input().split()))

    min_V = 1987654321
    max_V = -1987654321

    DFS(1,numbers[0])
    result = max_V - min_V
    print('#{} {}'.format(test_case,result))


