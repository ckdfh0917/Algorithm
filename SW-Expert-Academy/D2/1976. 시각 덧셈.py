q = int(input())

for test_case in range(1, q + 1):
    hour1, minute1, hour2, minute2 = map(int, input().split())

    hour = hour1 + hour2
    minute = minute1 + minute2

    if hour > 12:
        hour = hour - 12

    if minute > 60:
        hour += 1
        minute = minute - 60
    print('#{} {} {}'.format(test_case, hour, minute))