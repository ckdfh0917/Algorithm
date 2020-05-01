T = int(input())

for test_case in range(1, T+1):
    num = float(input())
    print('#{}' .format(test_case), end=' ')

    temp = 1
    res = []
    while True:
        if num == 0:
            break
        temp = temp / 2
        if num >= temp:
            num -= temp
            res.append(1)
        else:
            res.append(0)
    if len(res) >= 13:
        print('overflow')
    else:
        print(''.join(map(str, res)))

    # print(res)
