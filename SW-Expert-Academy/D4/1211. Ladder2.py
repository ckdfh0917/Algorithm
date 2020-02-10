import sys
sys.stdin = open('input.txt', 'r')



for test_case in range(1,11):
    q = int(input())
    lad = []
    for _ in range(100):
        temp = list(map(int, input().split()))
        lad.append(temp)
    # for i in range(100):
    #     print(lad[i])

    min_num = 1000
    idx = 0

    # 첫 시작점 찾기
    for k in range(100):
        cnt = 0
        if lad[0][k] == 1:
            start_point = k
            i, j = 0, k
            flag = 0
            #print('====={}====='.format(k))
            # 첫 시작점을 찾은 다음
            while 1:
                #print(i, j)
                # 오른쪽으로 가야할 때
                if j+1 <= 99 and lad[i][j + 1] == 1 and flag == 1:
                    j += 1
                    flag = 1
                    cnt += 1
                # 왼쪽으로 가야할 때
                elif j-1 >= 0 and lad[i][j - 1] == 1 and flag == -1:
                    j -= 1
                    flag = -1
                    cnt += 1
                # 아래 오른쪽도 있을 때
                elif j+1 <= 99 and i+1 <= 99 and lad[i + 1][j + 1] == 1:
                    i += 1
                    flag = 1
                # 아래 왼쪽도 있을 때
                elif j-1 >= 0 and i+1 <= 99and lad[i + 1][j - 1] == 1:
                    i += 1
                    flag = -1
                # 아래만 있을 때
                elif lad[i][j] == 1:
                    i += 1

                if i == 100:
                    #print('c', k, i, cnt)
                    break

            if min_num > cnt:
                min_num = cnt
                idx = k
                #print('a', min_num, idx)
    print('#{} {}' .format(test_case, idx))