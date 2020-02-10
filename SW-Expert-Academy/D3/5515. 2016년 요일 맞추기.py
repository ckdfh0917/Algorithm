import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

day = [31,29,31,30,31,30,31,31,30,31,30,31]
days = [3,4,5,6,0,1,2]
for test_case in range(1,q+1):
    m, d = map(int, input().split())
    print('#{} ' .format(test_case), end='')
    sum_day = 0
    for i in range(m-1):
       sum_day += day[i]
    sum_day += d
    #print(sum_day)

    res = sum_day % 7
    print(days[res])
