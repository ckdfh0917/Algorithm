import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    A, B, C = map(int, input().split())

    cnt = 0

    while C >= min(A,B):
        C -= min(A,B)
        cnt += 1
    print('#{} {}' .format(test_case, cnt))