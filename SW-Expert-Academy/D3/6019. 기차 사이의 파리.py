import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    D, A, B, F = map(int, input().split())

    # 충돌하는 시간
    t = D / (A+B)
    #print(t)

    # 파리 이동 거리
    res = F * t
    #print(res)
    print('#{} {}' .format(test_case, res))