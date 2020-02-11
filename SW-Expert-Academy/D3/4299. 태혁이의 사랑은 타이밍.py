import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    D, H, M = map(int, input().split())
    print('#{} ' .format(test_case), end='')
    res = 0
    res += (D - 11) * 24 * 60
    res += (H - 11) * 60
    res += (M - 11)
    if res >= 0:
        print(res)
    else:
        print(-1)
