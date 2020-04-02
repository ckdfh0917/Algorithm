q = int(input())

for test_case in range(1,q+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        temp = numbers.pop(0)
        numbers.append(temp)
    print('#{} {}'.format(test_case, numbers[0]))