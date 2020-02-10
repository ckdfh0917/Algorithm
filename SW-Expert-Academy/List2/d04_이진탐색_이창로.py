import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def binarySearch(front, end, search, count):
    c = (front + end) // 2
    #print(front, end, search, count)
    if search > c:
        front = c
        count += 1
        return binarySearch(front, end, search, count)
    elif search < c:
        end = c
        count += 1
        return binarySearch(front, end, search, count)
    elif search == c:
        return count


for test_case in range(1,q+1):
    P, A, B = map(int, input().split())
    countA, countB = 0, 0
    print('#{}'.format(test_case), end=' ')
    result_a = binarySearch(1,P,A,countA)
    result_b = binarySearch(1,P,B,countB)
    if result_a > result_b:
        print('B')
    elif result_a < result_b:
        print('A')
    else:
        print('0')