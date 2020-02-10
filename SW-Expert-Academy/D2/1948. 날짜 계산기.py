q = int(input())

month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, q + 1):
    month1, day1, month2, day2 = map(int, input().split())
    print('#{} '.format(test_case), end='')
    arr = []

    if month1 == month2:
        result = day2 - day1 + 1
    else:
        for i in range(1, 13):
            if month1 < i < month2:
                arr += [i]

        sum_day = 0
        for i in arr:
            sum_day += month_dict[i]
        # print(sum_day)
        sum_day = sum_day + month_dict[month1] - day1 + 1
        # print(month_dict[month1] - day1 + 1)
        sum_day += day2
        # print(day2)
        result = sum_day
    print(result)