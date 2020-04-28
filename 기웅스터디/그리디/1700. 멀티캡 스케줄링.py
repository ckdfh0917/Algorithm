N, K = map(int, input().split())

num = list(map(int, input().split()))
stack = []
visited = [0] * (K+1)
cnt = 0
for i in range(K):
    print(stack, num[i], visited, cnt)
    fluggedin = False
    if len(stack) < N:
        stack.append(num[i])
        # visited[num[i]] = 1
    else:
        if num[i] in stack:
            print('bbb', num[i])
            continue
        flag = 0
        for j in range(N):
            if i+j < K:
                print('aa',i,j,i+j)
                if num[i+j] in stack:
                    visited[num[i+j]] = 1
        for j in range(len(stack)):
            if visited[stack[j]] == 0:
                stack[j] = num[i]
                cnt += 1
                flag = 1
                break

print(cnt)


