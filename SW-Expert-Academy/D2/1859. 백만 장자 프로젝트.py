import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    day = int(input())
    days = list(map(int, input().split()))

    print('#{} ' .format(test_case), end ='')
    buy = []
    money = []
    sell = 0

    max_money = max(days)
    for i in range(0,day):
        if days[i] < max_money:
            #print('max {}' .format(max(days)))
            buy.append(days[i])
            #print('buy {}'.format(buy))
        elif days[i] == max_money:
            #print('max {}'.format(max(days)))
            sell = days[i]
            days[i] = 0
            max_money = max(days[i:])
            #print('sell {}'.format(sell))
        if sell != 0:
            for j in range(len(buy)):
                money.append(sell-buy.pop(0))
                #print('money {}' .format(money))
            sell = 0


    result = sum(money)

    print('{}' .format(result))