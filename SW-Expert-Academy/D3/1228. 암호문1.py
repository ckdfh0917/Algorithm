for test_case in range(1, 11):
    n = int(input())
    num = list(map(int, input().split()))
    k = int(input())
    command = list(map(str, input().split()))

    for i in range(len(command)):
        if command[i] == 'I':
            a = int(command[i+1])
            b = int(command[i+2])
            temp = []
            for j in range(i+3, i+2+b+1):
                num.insert(a, int(command[j]))
                a += 1
    print('#{} '.format(test_case), end='')
    print(' '.join(map(str, num[0:10])))