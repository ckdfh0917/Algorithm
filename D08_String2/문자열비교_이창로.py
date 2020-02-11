q = int(input())

for test_case in range(1, q+1):
    str1 = input()
    str2 = input()

    print('#{} ' .format(test_case), end='')
    flag = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            print(1)
            flag = 1
            break
    if flag == 0:
        print(0)