import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def getSubset(lst,K):
    n = len(lst)
    result = []
    for i in range(1<<n):
        res = []
        for j in range(n):
            temp = i & (1<<j)
            if temp:
                res.append(lst[j])
        sum_V = 0
        sum_C = 0
        if res:
            flag = 0
            # print('r',res)
            # print('l',len(res))
            for k in range(len(res)):
                sum_V += res[k][0]
                sum_C += res[k][1]
                if sum_V > K:
                    flag = 1
                    break
            if flag == 0:
                result.append(sum_C)
    return result

for test_case in range(1,q+1):
    N, K = map(int, input().split())

    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    # print(box)
    # print(box[0][0])
    a = []
    V = []

    arr = getSubset(box,K)
    # print('qqqq',arr)

    max_t = max(arr)
    print('#{} {}' .format(test_case, max_t))