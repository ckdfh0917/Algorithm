T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M-1):
        temp = list(map(int,input().split()))
        flag = 0
        for j in range(N):
            if temp[0] < numbers[j]:
                flag = 1
                tempA = numbers[0:j]
                tempB = numbers[j:]
                tempA.extend(temp)
                tempA.extend(tempB)
                numbers = tempA[:]
                break
        if flag == 0:
            numbers.extend(temp)
    result = numbers[-10:-1]
    result.append(numbers[-1])
    result.reverse()
    print('#{} ' .format(test_case), end='')
    print(' '.join(map(str, result)))