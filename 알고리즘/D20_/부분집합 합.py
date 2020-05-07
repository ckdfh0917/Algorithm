n = [-1,3,-9,6,7,-6,1,5,4,-2]

def subset(lst):
    k = len(lst)
    result = []
    for i in range(1 << k):
        temp = []
        for j in range(k):
            a = i & (1 << j)
            if a:
                temp.append(lst[j])
        if sum(temp) == 0:
            result.append(temp)
    return result

print(subset(n))
