import sys
sys.stdin = open('input.txt','r')

q = int(input())

for test_case in range(1,q+1):
    num = input()
    print('#{} '.format(test_case), end='')
    #print(len(num))
    flag = 0

    k = num
    list_a = [0] * 10
    #print(list_a)
    result = 1
    temp = 0
    while result < 100:
        k = str(k)
        #print(k)
        for i in range(len(k)):
            #print('a')
            for j in range(10):
                p = int(k[i])
                if p == j:
                    #print('b')
                    list_a[j] += 1
                    #print(list_a)
        temp = 0
        for i in range(10):

            if list_a[i] != 0:
                temp += 1
            #print('temp {}' .format(temp))
            if temp > 9:
                flag = 1
                break
        if flag == 1:
            break
        result += 1
        k = int(num) * result
        #print(k)
    print(k)