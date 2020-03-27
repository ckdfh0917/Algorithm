def getSubset(lst):
    n = len(lst)
    result = []
    for i in range(1 << n):
        temp = []
        for j in range(n):
            a = i & (1 << j)
            if a:
                temp.append(lst[j])
        result.append(temp)
    return result

