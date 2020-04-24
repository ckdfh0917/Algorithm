N, K = map(int, input().split())

num = list(map(int, input().split()))
stack = []
visited = [0] * (K+1)
for i in range(K):
    if len(stack) < N:
        stack.append(num[i])
    else:
        flag = 0
        for j in range(N):
            if i+j < K:
                if num[i+j] in stack:
                    visited[num[i+j]] = 1
        for j in range(len(stack)):
            if stack[j] not in visited:
                stack[j] = num[i]
                flag = 1
                break

        if flag == 0:
            for x in range(i+1, K):
                visited[num[x]] =