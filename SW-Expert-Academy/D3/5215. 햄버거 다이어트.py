import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def getSubset(lst):
    n = len(lst)
    result = []
    for i in range(1<<n):
        res = []
        for j in range(n):
            temp = i & (1<<j)
            if temp:
                res.append(lst[j])
        result.append(res)
    return result

for test_case in range(1, q+1):
    N, L = map(int, input().split())    # N: 재료수, L: 제한 칼로리

    menu = []
    for i in range(N):
        temp = list(map(int, input().split()))
        if temp[1] <= L:
            menu.append(temp)
    #print(menu)

    subset_menu = getSubset(menu)

    a = []
    idx = 0
    maxTT = 0
    for i in range(len(subset_menu)):
        sumT = 0
        sumK = 0
        flag = 0
        for j in range(len(subset_menu[i])):
            sumT += subset_menu[i][j][0]
            sumK += subset_menu[i][j][1]
            if sumK > L:
                flag = 1
                break
            if maxTT < sumT:
                maxTT = sumT
        if flag == 0:
            temp = [sumT] + [sumK]
            #print(temp)
            a.append(temp)
    #print(a)
    print('#{} {}'.format(test_case, maxTT))