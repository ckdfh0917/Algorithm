N = int(input())
numbers = list(map(int, input().split()))

idx = 0
i = 0
result = []
visited = [False] * N
for i in range(N):

    if not visited[idx]:
        visited[idx] = True
        result.append(idx+1)
        temp = 0
        k = idx
        # print('aa',i + 1, idx)
        if all(visited):
            continue
        if numbers[idx] > 0:
            while temp < numbers[k]:
                # print('+',temp, numbers[idx])
                if idx+1 == N:
                    idx =0
                if not visited[idx+1]:
                    idx += 1
                    temp += 1
                else:
                    idx += 1
        else:
            while temp > numbers[k]:
                # print('-',temp, idx, numbers[idx])
                if idx == 0:
                    idx = N
                if not visited[idx-1]:
                    idx -= 1
                    temp -= 1
                else:
                    idx -= 1
        # print('a',result)

print(' '.join(map(str, result)))
