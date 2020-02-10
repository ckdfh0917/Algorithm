import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N, K = map(int, input().split())

    numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

    n = len(numbers)
    ans = 0
    for i in range(1 << n):
        sum = 0
        temp = 0
        for j in range(n):
            if i & (1 << j):
                sum += numbers[j]
                temp += 1
        #print(sum, temp)
        if sum == K and temp == N:
            ans += 1

    print('#{} {}'.format(test_case, ans))
