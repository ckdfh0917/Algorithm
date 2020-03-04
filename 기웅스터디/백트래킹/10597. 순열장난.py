num = input()
visited = [True] + [False] * 60
result = []
a = []
def dfs(idx):
    global flag
    if idx > len(num)-1:
        # print('a', result)
        for i in range(1,len(result)+1):
            if not visited[i]:
                return False
        print(' '.join(map(str, result)))
        flag = 1
        return True
    n = int(num[idx])
    # print(result)
    # print('z', n)

    if n > 0:
        if not visited[n]:
            visited[n] = True
            result.append(n)
            if dfs(idx+1):
                return
            if flag == 1:
                return
            # print('p', result)
            result.pop()
            visited[n] = False

    if n <= 5:
        if idx+1 < len(num):
            n = int(num[idx:idx+2])
            # print('v', n)
            if not visited[n]:
                visited[n] = True
                result.append(n)
                if dfs(idx+2):
                    return
                if flag == 1:
                    return
                # print('k',result)
                result.pop()
                visited[n] = False
flag = 0
dfs(0)