q = int(input())

def promissing(level):   # 체스말을 놓을 수 있는지 없는지 판단하는 함수
    # 같은 열, 같은 대각선 여부 판단: True, False 리턴
    for i in range(1,level):
        if cols[i] == cols[level] or (level - i) == abs(cols[i] - cols[level]):
            return False
    return True

def queen(level):
    global cnt
    print(level)
    print(cols)
    if promissing(level) == False:   # 백트래킹
        return
    # 재귀호출로 각 행에 체스를 놓기
    elif level == N:
        # print('a')
        cnt += 1
        return
    else:
        for i in range(1,N+1):
            cols[level+1] = i
            queen(level+1)
for test_case in range(1,q+1):
    N = int(input())

    cnt = 0
    cols = [0] * (N+1)  # 1-N행 : 몇번째 열에 체스가 놓여있는지
    queen(0)
    print('#{} {}'.format(test_case, cnt))
