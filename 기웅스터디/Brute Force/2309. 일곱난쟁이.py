man = [int(input()) for _ in range(9)]
# print(man)
def getSubset(lst):
    n = len(lst)
    result = []
    for i in range(1<<n):
        temp = []
        for j in range(n):
            a = i & (1<<j)
            if a:
                temp.append(lst[j])
        if len(temp) == 7 and sum(temp) == 100:
            result.append(temp)
            result[0].sort()
    print(' '.join(map(str,result[0])))

getSubset(man)