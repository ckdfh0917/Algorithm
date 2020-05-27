N = int(input())
K = int(input())
lst = list(map(int, input().split()))

lst.sort()
lst = list(set(lst))
res = []
tmp = []
minV = 1234567891
visited = [0] * len(lst)
visited[-1] = 1
print(lst)
def find(v, idx, ans):
    global res, minV
    print('a', v, idx, ans)
    if v.count(1) == K:

        return
    elif ans > minV:
        print('back')
        return
    else:
        index = 0
        for i in range(idx, len(v)):
            # print('i', i)
            if v[i] == 0:
                v[i] = 1
                print(i, index, lst[i], lst[index])
                find(v, i + 1, ans + lst[i] - lst[index])
                v[i] = 0
                index = i
find(visited, 0, 0)
print('==============')
print(minV)



