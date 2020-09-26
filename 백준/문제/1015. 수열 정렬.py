N = int(input())
A = list(map(int, input().split()))
B = sorted(A)

P = [0] * N
visited = [0] * N

for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            P[i] = j
            break

print(P)
for i in range(N):
    # print('v', P[i], visited)
    if visited[P[i]] == 0:
        visited[P[i]] = 1
    else:
        idx = 1
        while P[i] == P[i+idx]:
            if visited[P[i+idx]] == 0:
                visited[P[i+idx]] = P[idx] + idx
                P[i+idx] += idx
            else:
                idx += 1
print(P)