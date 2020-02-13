import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(1,11):
    q = int(input())    # 쓰레기값
    print('#{} '.format(test_case), end='')
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 도착점 찾기
    k = 0
    for j in range(100):
        if arr[99][j] == 2:
            k = j
            break

    i = 98
    #print(k)
    flag = 0
    #print('====={}====='.format(k))
    # 첫 시작점을 찾은 다음
    while 1:
        #print(i, k)
        # 오른쪽으로 가야할 때
        if k + 1 <= 99 and arr[i][k + 1] == 1 and flag == 1:
            k += 1
            flag = 1
        # 왼쪽으로 가야할 때
        elif k - 1 >= 0 and arr[i][k - 1] == 1 and flag == -1:
            k -= 1
            flag = -1
        # 위 오른쪽도 있을 때
        elif k + 1 <= 99 and arr[i - 1][k + 1] == 1: #and i - 1 >= 0
            i -= 1
            flag = 1
        # 위 왼쪽도 있을 때
        elif k - 1 >= 0 and arr[i - 1][k - 1] == 1: #and i - 1 >= 0
            i -= 1
            flag = -1
        # 아래만 있을 때
        elif arr[i][k] == 1:
            i -= 1

        if i == 0:
            result = k
            break

    print(result)