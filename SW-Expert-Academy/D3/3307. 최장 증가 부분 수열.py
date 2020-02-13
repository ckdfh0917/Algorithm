import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_cnt = 0
    for i in range(n):
        temp = arr[i]
        temp2 = arr[i]
        cnt = 0
        flag = 0
        for j in range(i,n):
            if temp <= arr[j]:
                print(arr[j], end=' ')
                temp = arr[j]
                cnt += 1
        for j in range(i-1,-1,-1):
            if arr[j] <= temp2:
                cnt+=1
                print(arr[j], end=' ')
                temp2 = arr[j]
        print()
        if max_cnt < cnt:
            max_cnt = cnt
    print('#{} {}'.format(test_case, max_cnt))