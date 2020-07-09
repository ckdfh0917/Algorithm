N, M = map(int, input().split())
numbers = list(map(int, input().split()))

def f(mid):
    sum = 0
    num = 1

    for i in range(N):
        if numbers[i] > mid:
            return False

        sum += numbers[i]
        if sum > mid:
            sum = numbers[i]
            num += 1

    return M >= num


s = 1
e = sum(numbers)
res = 0

while s <= e:
    mid = (s+e) // 2

    if f(mid):
        res = mid
        e = mid - 1
    else:
        s = mid + 1

print(res)