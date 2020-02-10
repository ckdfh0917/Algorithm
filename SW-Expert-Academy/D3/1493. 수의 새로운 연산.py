import sys
sys.stdin = open('input.txt', 'r')

q = int(input())


# 열 찾기
def find_col(n, a_list):
    for i in range(20000):
        #print(n, a[i])
        if n > a[i]:
            continue
        elif n < a[i]:
            return i, a[i-1]
        elif n == a[i]:
            return i+1, a[i]

def find_num(n, idx, col):
    cnt = 0
    for i in range(idx):
        if col == n:
            return cnt
        else:
            cnt += 1
            col += 1

for test_case in range(1,q+1):
    x, y = map(int, input().split())
    print('#{} ' .format(test_case), end='')
    # 첫번째 열 만들기
    a = [0 for _ in range(20000)]
    cnt = 1
    a[0] = 1
    for i in range(1,20000):
        a[i] = a[i-1] + cnt
        cnt += 1

    # x
    idx, col = find_col(x,a)        # 찾는 인덱스와 열의 값을 반환
    cnt = find_num(x, idx, col)     # 몇 칸 더 이동해야 찾는 숫자가 나오는지 반환
    # 해당되는 숫자의 좌표
    X1 = cnt + 1
    Y1 = idx - cnt

    # y
    idx, col = find_col(y, a)       # 찾는 인덱스와 열의 값을 반환
    cnt = find_num(y, idx, col)     # 몇 칸 더 이동해야 찾는 숫자가 나오는지 반환
    # 해당되는 숫자의 좌표
    X2 = cnt + 1
    Y2 = idx - cnt

    newX = X1 + X2
    newY = Y1 + Y2

    temp = 0
    # 0번째 열까지의 칸 수
    for i in range(20000):
        if newX == 0:
            break
        else:
            newX -= 1
            temp += 1
    # 대각선으로 가서 0번째 칸에 있는 열 찾기
    reY = newY + temp - 2
    print(a[reY]+temp-1)