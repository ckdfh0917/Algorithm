import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def promissing(level):   # 체스말을 놓을 수 있는지 없는지 판단하는 함수
    # 같은 열, 같은 대각선 여부 판단: True, False 리턴
    for i in range(1,level):
        #현재놓여진 말의 정보 cols[level]
        #이제까지 놓여진 말의 정보 cols[i]
        #같은 열이면 X, 대각선이어도 X
        if cols[i] == cols[level] or (level - i) == abs(cols[i] - cols[level]):
            return False
    return True

def queen(level):
    global cnt
    # print('q')
    if promissing(level) == False:  # 백트래킹 #유망성 검사
        return                      # 검사후 가망이 없으면 이전으로 리턴
    # 재귀호출로 각 행에 체스를 놓기
    elif level == N:                # 현재 레벨이 마지막행이라면
        # print('a')
        cnt += 1
        return
    else:
        for i in range(1,N+1):
            cols[level+1] = i       # 다음행 확인하기 : 다음행에 i 넣고
            queen(level+1)          #재귀호출   -> 재귀에서 돌아오면 다시 반복 (i증가)
for test_case in range(1,q+1):
    N = int(input())

    cnt = 0
    cols = [0] * (N+1)  # 1-N행 : 몇번째 열에 체스가 놓여있는지
    queen(0)
    print('#{} {}'.format(test_case, cnt))
