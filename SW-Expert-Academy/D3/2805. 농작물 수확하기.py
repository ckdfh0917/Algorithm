import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

dx = [-1,0,1,0]     # 위 오른 아래 왼
dy = [0,1,0,-1]

for test_case in range(1,q+1):
    num = int(input())

    arr = []
    for i in range(num):
        arr.append(list(map(int, input().split())))
    print(arr)
    temp = 0
    for i in range(num//2+1):
        j = 1
        k = 1
        print('i',i)
        print('n', num//2 +k)
        while j < num//2 + k:
            print('j',j,num // 2 + k + j,num//2+k-j)
            temp += arr[i][num // 2 + k + j] + arr[i][num//2+k-j]
            j += 1
            print(temp)
        k += 1
        print(temp)

    for i in range(num//2+1,num):
        pass