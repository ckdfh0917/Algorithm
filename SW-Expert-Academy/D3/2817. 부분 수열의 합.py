import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def getSubset(lst):
    n = len(lst)
    cnt = 0
    for i in range(1<<n):
        a = 0
        for j in range(n):
            temp = i & (1<<j)
            if temp:
                a += lst[j]
        if a == K:
            cnt += 1
    return cnt

for test_case in range(1, q+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = getSubset(A)
    #print(n_list)

    print('#{} {}'.format(test_case,result))
