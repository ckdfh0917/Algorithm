import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    A, B = input().split()

    flag = False
    cnt = 0
    for i in range(len(A)):
        if flag == False:
            j = 0
        flag = False
        while j < len(B):
            #print('#',A[i],B[j])
            if A[i] == B[j]:
                #print(A[i])
                j += 1
                cnt += 1
                flag = True
                break
            else:
                j += 1
    print('#{} {}'.format(test_case,cnt))
