N, S = map(int, input().split())
numbers = list(map(int, input().split()))

def GetSubset(lst):
    n = len(lst)
    result = []
    # zz = []
    cnt = 0
    for i in range(1<<n):
        temp = []
        for j in range(n):
            a = i & (1 << j)
            if a:
                temp.append(lst[j])
        result.append(temp)
        # zz.append(sum(result[i]))
        if result[i] and sum(result[i]) == S:
            cnt += 1
    # print(result)
    # print(zz)
    return cnt

print(GetSubset(numbers))
