q = int(input())

for test_case in range(1,q+1):
    price = list(map(int, input().split()))
    months = list(map(int, input().split()))


    result = 987654321
    # 매일
    temp = 0
    for i in range(12):
        temp += months[i] * price[0]
    # print('a',temp)
    result = min(result, temp)
    # 매달
    temp = 0
    for i in range(12):
        if months[i] > 0:
            temp += price[1]
    # print('b', temp)
    result = min(result, temp)
    # 매년
    temp = price[3]
    print('c', temp)
    # result = min(result, temp)
    # 섞어서
    temp = 0
    i = 1
    while i < 12:
        print(i, temp)
        if i < 10 and months[i] != 0 and price[2] < (months[i] + months[i+1] + months[i+2])*price[0]:
            if price[2] < price[1] * 3:
                if price[1] < price[0] * months[i]:
                    if i < 9 and months[i] > months[i+3]:
                        # print(months[i], months[i+3])
                        temp += price[2]
                        i += 3
                    continue
                if price[1] >= price[0] * months[i]:
                    temp += price[0] * months[i]
                    i += 1
                    continue
        if months[i] != 0 and months[i] * price[0] < price[1]:
            temp += months[i] * price[0]
            i += 1
            continue
        if months[i] != 0:
            temp += price[1]
            i += 1
            continue
        i += 1
    print('d', temp)
    result = min(result, temp)
    print(result)
