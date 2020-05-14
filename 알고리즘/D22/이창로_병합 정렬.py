T = int(input())

def merge(left, right):
    global cnt
    result = []
    flag = 0
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                temp = left.pop(0)
                result.append(temp)
            else:
                temp = right.pop(0)
                result.append(temp)
        elif len(right) > 0:
            temp = right.pop(0)
            result.append(temp)
        elif len(left) > 0:
            temp = left.pop(0)
            result.append(temp)
            flag = 1
    if flag == 1:
        cnt += 1
    return result

def merge2(left, right):
    global cnt
    result = []
    flag = 0
    i = j = 0
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif len(right) > j:
            result.append(right[j])
            j += 1
        elif len(left) > i:
            result.append(left[i])
            i += 1
            flag = 1
    if flag == 1:
        cnt += 1
    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge2(left, right)


for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    ans = merge_sort(numbers)
    res = ans[N//2]
    print('#{} {} {}'.format(test_case, res, cnt))