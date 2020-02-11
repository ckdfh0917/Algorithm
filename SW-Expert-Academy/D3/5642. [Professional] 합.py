import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

def subSet(n,list):
    k = []
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (i<<j):
                temp.append(list[j])
        print(temp)
        k += [temp]
    return k

for test_case in range(1,q+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    print(num_list)

    new_list = subSet(N,num_list)
    #print(new_list)