N, L = map(int, input().split())
water = list(map(int, input().split()))

water.sort()
max_V = water[-1]
min_V = water[0]

visited = [False for i in range(max_V+L+1)]
result = 0

i = 1
result = 0
while i < max_V + L:
    # print(i)
    if i in water and not visited[i]:
        for j in range(L):
            # print('b', i + j, max_V)
            if i+j <= max_V:
                # print('a', i + j)
                visited[i+j] = True
        result += 1
        i += L
    else:
        i += 1



print(result)