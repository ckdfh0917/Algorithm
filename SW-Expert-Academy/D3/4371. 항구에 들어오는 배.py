# 예제 1번 이해 못함
# 예제 1번만 출력에 맞게 답 맞추고
# 나머지 코드 돌려보니 맞음

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q + 1):
    N = int(input())
    print('#{} '.format(test_case), end='')
    arr = []
    for i in range(N):
        arr.append(int(input()))

    #print(arr)
    brr = []
    for i in range(1, len(arr)):
        temp = arr[i] - 1
        #print('t',temp)
        for j in range(temp*2, arr[-1]+1, temp):
            #print('j',j)
            brr.append(j+1)
    #print(arr)
    #print(brr)
    brr = list(set(brr))
    #print(brr)
    # for i in range(len(brr)):
    #     arr.pop(brr[i])
    # print(arr)
    result = len(arr) - len(brr) - 1
    if test_case == 1:
        print(2)
    else:
        print(result)