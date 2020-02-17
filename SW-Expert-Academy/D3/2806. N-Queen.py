import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def promissing():   # 체스말을 놓을 수 있는지 없는지 판단하는 함수
    # 같은 열, 같은 대각선 여부 판단: True, False 리턴
    for i in range(1,N+1):
        # print('d',i)
        if cols.count(i) > 2:
            return False
        for j in range(cols[i]+2,N+1):
            # print('c',j,N+1)
            if i-1 >= 1 and i+1 <= N:
                # print('k',i-1,i+1,N)
                # print('b',i+1,cols[i-1],cols[i+1])
                if cols[i-1] == i+1 or cols[i+1] == i+1:
                    return False
    return True

def queen(level):
    global cnt
    # print('q')
    if promissing() == False:   # 백트래킹
        print(cols)
        return
    # 재귀호출로 각 행에 체스를 놓기
    elif level == N:
        # print('a')
        cnt += 1
        return
    else:
        print('u',N+1)
        for i in range(1,N+1):
            print('la',level)
            cols[level] = 1
            print('z')
            queen(level+i)
            print('cx')
for test_case in range(1,q+1):
    N = int(input())
    print('#{} '.format(test_case))

    cnt = 0
    cols = [0] * (N+1)  # 1-N행 : 몇번째 열에 체스가 놓여있는지
    print(cols)
    queen(1)
    print('#{} {}'.format(test_case, cnt))
