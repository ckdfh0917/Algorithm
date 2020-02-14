import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def min_max(numbers, max1, min1, max2, min2):
    for i in range(len(numbers)):
        if max2 < numbers[i] < max1:
            max2 = numbers[i]
        if min1 < numbers[i] < min2:
            min2 = numbers[i]
    return max2, min2

# for test_case in range(1,q+1):
#     n = int(input())
#     numbers = list(map(int, input().split()))
#
#     print('#{} '.format(test_case), end='')
#
#     #print(numbers)
#     max_num = 101
#     min_num = 0
#     for _ in range(5):
#         max_num, min_num = min_max(numbers, max_num, min_num, 0, 101)
#         print('{} {} ' .format(max_num,min_num) , end='')
#     print()

for test_case in range(1,q+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    print('#{} '.format(test_case), end='')

    numbers.sort()
    #print(numbers)

    k = 0
    for i in range(10):
        if i % 2 == 0:
            print('{}' .format(numbers[-k-1]), end=' ')
        elif i % 2 == 1:
            print('{}' .format(numbers[k]), end=' ')
            k += 1
    print()