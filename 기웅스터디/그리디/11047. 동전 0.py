N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
# print(coin)

result = 0
while K != 0:
    a = 0
    for x in coin:
        if x <= K:
            a = x
        else:
            break
    result += K // a
    K -= (K//a) * a
print(result)