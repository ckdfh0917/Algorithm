N, K = map(int, input().split())

d = [0] * (K+10)
w = [0] * 101
v = [0] * 101

def dp():
    for i in range(N+1):
        for j in range(K+1, -1, -1):
            # print('a', i, j)
            if w[i] < j:
                # print('a',i, j)
                # print('w', d[j], d[j-w[i]], v[i], d[j-w[i]] + v[i])
                d[j] = max(d[j], d[j-w[i]] + v[i])
    #         print('j', d)
    # print(d)
    print(d[K+1])


for i in range(N):
    w[i], v[i] = map(int, input().split())

dp()

