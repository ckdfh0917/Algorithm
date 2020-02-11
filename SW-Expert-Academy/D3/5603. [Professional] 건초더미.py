import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N = int(input())

    gun = []
    for i in range(N):
        gun.append(int(input()))
    k = sum(gun)//N
    cnt = 0
    for i in gun:
        if i > k:
            cnt += i-k
    print('#{} {}'.format(test_case,cnt))