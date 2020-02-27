N = int(input())
budget = list(map(int, input().split()))
M = int(input())


def find(min_V, max_V):
    mid = (min_V + max_V) // 2
    if min_V > max_V:
        print(mid)
        return
    else:
        sum_V = 0
        for i in range(N):
            if mid >= budget[i]:
                sum_V += budget[i]
            else:
                sum_V += mid
        if sum_V == M:
            print(mid)
            return
        elif sum_V < M:
            find(mid+1,max_V)
        elif sum_V > M:
            find(min_V, mid-1)
        # print('b',min_V,mid,max_V)

k = sum(budget)
result = 0
if k <= M:  # 총 예산이 예산 요청의 합 보다 크면 원하는 만큼 준다
    result = max(budget)
    print(result)
else:       # 총 예산이 예산 요청의 합 보다 작으면
    find(1,10**5)
