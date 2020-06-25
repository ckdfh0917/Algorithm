L, C = map(int, input().split())
code = list(input().split())

code.sort()

def get_subset(idx, v):
    # print(v)
    if v.count(1) == L:
        res.append(v[:])
    else:
        for i in range(idx, C):
            if v[i] == 0:
                v[i] = 1
                if i == C-1:
                    if v.count(1) < L:
                        v[i] = 0
                        return
                if v in res:
                    v[i] = 0
                else:
                    get_subset(i, v)
                    v[i] = 0
    return


visited = [0] * C

res = []
get_subset(0, visited)
# print(res)

ans = []
mm = ['a', 'e', 'i', 'o', 'u']
for x in res:
    temp = ''
    for i in range(C):
        if x[i] == 1:
            temp += code[i]
    flag = 0
    for x in temp:
        if x in mm:
            flag += 1
            break
    cnt = 0
    for x in temp:
        if x not in mm:
            # print(x, temp)
            flag += 1
            cnt += 1
        if cnt == 2:
            break

    if flag == 3:
        ans.append(temp)

print('\n'.join(ans))