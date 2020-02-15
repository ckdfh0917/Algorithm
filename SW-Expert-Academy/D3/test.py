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

for test_case in range(1,q+1):
    N, K = map(int, input().split())

    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))

    arr = getSubset(box)
    max_C = 0
    for i in range(1,len(arr)):
        sum_V = 0
        sum_C = 0
        flag = 0
        for j in range(len(arr[i])):
            sum_V += arr[i][j][0]
            sum_C += arr[i][j][1]
            if sum_V > K:
                flag = 1
                break
        if flag == 0:
            if max_C < sum_C:
                print(arr[i])
                max_C = sum_C

    #print('qqqq',res)

    print('#{} {}' .format(test_case, max_C))