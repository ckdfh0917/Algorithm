import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    a = N
    k = []
    for i in range(N):
        a = 1
        while a < N:
            temp = 0
            for j in range(i,a+1):
                temp += num_list[j]
            a += 1
            #print(temp)
            k.append(temp)
            #print(k)
    print('#{} {}' .format(test_case, max(k)))