t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    k = 0
    if nums[0] > 0:
        k = 1
    elif nums[0] < 0:
        k = -1

    result = []
    temp = []
    for i in range(n):
        # print(nums[i])
        if nums[i] > 0:
            if k == 1:
                temp.append(nums[i])
            elif k == -1:
                result.append(max(temp))
                temp = [nums[i]]
            k = 1
        elif nums[i] < 0:
            if k == 1:
                result.append(max(temp))
                temp = [nums[i]]
            elif k == -1:
                temp.append(nums[i])
            k = -1
        # print(temp)
        # print(result)
        # print('===================')
    if k == 1 and temp[0] > 0:
        result.append(max(temp))
    elif k == -1 and temp[0] < 0:
        result.append(max(temp))
    elif k == 1 and temp[0] < 0:
        result.append(max(temp))
    elif k == -1 and temp[0] > 0:
        result.append(max(temp))
    print(sum(result))
    # print(result, 'bbbbbbbbbbbbbbbb')