N = int(input())
budget = list(map(int, input().split()))
M = int(input())

k = sum(budget)
max_V = max(budget)
min_V = 0
result = 0
temp = max_V // 2
if k <= M:  # 예산 이내이면
    result = max(budget)
    print('a')
elif min(budget) > M // N:  # 예산의 최저보다 총 예산 1/ N 이 작으면
    result = M // N
    print('b')
else:       # 예산 초과이면
    while True:
        k = temp * N
        # print('k',k,M)
        # print('t1',temp, min_V, max_V)
        if k > M:
            max_V = temp
            temp = (min_V + temp) // 2
        elif k < M:
            min_V = temp
            temp = (temp + max_V) // 2
        # print('t2',temp, min_V, max_V)
        if min_V + 1 == max_V:
            result = min_V
            break

# print(result * N)
a = result * N
cnt = 0
for i in range(N):
    if budget[i] <= result:
        a -= budget[i]
        cnt += 1
# print(a)
res = a // (N-cnt)
print(res)