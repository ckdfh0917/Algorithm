import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def getSubset(lst,K):
    n = len(lst)
    max_C = 0
    for i in range(1<<n):
        res = []
        for j in range(n):
            temp = i & (1<<j)
            if temp:
                res.append(lst[j])
        if res:
            flag = 0
            sum_V = 0
            sum_C = 0
            for k in range(len(res)):
                sum_V += res[k][0]      # 부피
                sum_C += res[k][1]      # 가치
                if sum_V > K:
                    flag = 1
                    break
            if flag == 0:
                print(res)
                if max_C < sum_C:
                    max_C = sum_C
    return max_C

for test_case in range(1,q+1):
    N, K = map(int, input().split())

    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))

    res = getSubset(box,K)
    #print('qqqq',res)

    print('#{} {}' .format(test_case, res))