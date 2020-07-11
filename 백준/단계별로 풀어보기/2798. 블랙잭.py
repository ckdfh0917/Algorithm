N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= M and res < temp:
                res = temp

print(res)