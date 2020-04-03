for test_case in range(10):
    q = int(input())
    num = list(map(int, input().split()))
    print('#{}' .format(q), end=' ')
    while True:
        for k in range(1, 6):
            if num[-1] <= 0:
                num[-1] = 0
                break
            else:
                temp = num.pop(0)
                temp -= k
                num.append(temp)
        if num[-1] == 0:
            break
    print(' '.join(map(str, num)))