import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def getSubset(lst):
    n = len(lst)
    global result
    for i in range(1<<n):
        res = []
        for j in range(n):
            temp = i & (1<<j)
            if temp:
                res.append(lst[j])
        if sum(res) >= S:
            result = min(result, sum(res)-S)
            # print(result)
            if result == 0:
                return
    return result

for test_case in range(1,q+1):
    N, S = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()    # 내림차순

    result = H[-1]
    # print(result)
    new_H = getSubset(H)

    print('#{} {}'.format(test_case,result))