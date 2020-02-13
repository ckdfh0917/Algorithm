import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

dx = [-1,0,1,0]     # 위 오른 아래 왼
dy = [0,1,0,-1]
#q = 1
for test_case in range(1,q+1):
    num = int(input())

    arr = []
    for i in range(num):
        arr.append(list(map(int, input())))
    #print(arr)
    temp1 = 0
    for i in range(0,num//2+1):
        k = 2*i + 1
        a = 0
        j = num//2 -i
        while a < k:
            #print(i, j, arr[i][j])
            temp1 += arr[i][j]
            a += 1
            j += 1
    #print(temp1)
    temp2 = 0
    #print()
    for i in range(num//2+1,num):   # 3, 4
        k = 2*(num-i-1) + 1
        a = 0
        j = num//2 -(num-1-i)
        while a < k:
            #print(i,j, arr[i][j])
            temp2 += arr[i][j]
            a += 1
            j += 1
            #print(temp2)
    res = temp1 + temp2
    print('#{} {}'.format(test_case,res))

    # 18 5