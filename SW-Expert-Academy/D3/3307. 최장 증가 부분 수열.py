import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    n = int(input())
    arr = list(input().split())

    max_cnt = 0
    for i in range(n):
        temp = arr[i]
        cnt = 0
        for j in range(i,n):
            if temp <= arr[j]:
                temp = arr[j]
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print('#{} {}'.format(test_case, max_cnt))