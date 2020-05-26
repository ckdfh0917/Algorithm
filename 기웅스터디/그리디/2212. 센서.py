N = int(input())
K = int(input())
lst = list(map(int, input().split()))

lst.sort()
lst = list(set(lst))
res = []
minV = 1234567891
visited = [0] * len(lst)
visited[-1] = 1
def find(v, idx, ans):
    global res, minV
    print(v, idx, ans)
    if v.count(1) == K:
        # print('v', v)
        cnt = 0
        idx = 0
        for i in range(len(v)):
            if cnt == K-1:
                res.append([lst[i], lst[-1]])
                break
            if v[i] == 1:
                if not res:
                    res.append([lst[0], lst[i]])
                    cnt += 1
                else:
                    res.append([lst[idx+1], lst[i]])
                    cnt += 1
                idx = i

        if len(res) == K:
            temp = 0
            flag = False
            for i in range(K):
                s, e = res[i]
                temp += e - s
                # if s == e:
                #     flag = True
            if not flag:
                minV = min(minV, temp)
                print(res)
                print(ans, temp)
                print(minV)
                print()
        res = []
        return
    elif ans > minV:
        print('back')
        return
    else:
        index = 0
        for i in range(idx, len(v)):
            # print('i', i)
            if visited[i] == 0:
                visited[i] = 1
                print(visited)
                if visited.count(1) == 1:
                    # print('ans0', lst[i] - lst[0])
                    find(v, i + 1, ans + lst[i] - lst[0])
                else:
                    # print('ans1', lst[i] - lst[index+1])
                    if visited.count(1) == K:
                        find(v, i + 1, ans + lst[i] - lst[index+1] + lst[-1] - lst[i+1] )
                    else:
                        find(v, i + 1, ans + lst[i] - lst[index+1])
                visited[i] = 0
                index = i
find(visited, 0, 0)
# print('==============')
print(minV)