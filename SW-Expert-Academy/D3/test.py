import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def getSubset(lst):
    n = len(lst)
    result = []
    a = []
    maxT = 0
    for i in range(1<<n):
        res = []
        for j in range(n):
            temp = i & (1<<j)
            if temp:
                res.append(lst[j])
        #print('r',res)
        maxTT = 0
        if res:
            sumT = 0
            sumK = 0
            for k in range(len(res)):
                sumT += res[k][0]
                sumK += res[k][1]
                if sumK > L:
                    break
                if sumT > maxT:
                    maxT = sumT
    return maxT

for test_case in range(1, q+1):
    N, L = map(int, input().split())    # N: 재료수, L: 제한 칼로리

    menu = []
    for i in range(N):
        temp = list(map(int, input().split()))
        if temp[1] <= L:
            menu.append(temp)

    maxTT = getSubset(menu)

    print('#{} {}'.format(test_case, maxTT))