N = int(input())
A = list(map(int, input().split()))
cnt = [1] * len(A)
res = 0

for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)
    res = max(res, cnt[i])

print(res)