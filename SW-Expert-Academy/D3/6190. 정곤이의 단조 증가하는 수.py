import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1, q+1):
    N = int(input())
    A = list(map(int, input().split()))
    #print('a',A)
    # A 숫자 리스트에서 두개씩 곱해서 B 리스트에 첨가
    B = []
    for i in range(N):
        for j in range(i+1,N):
            B.append(A[i] * A[j])
    #print('b',B)

    C = []
    for i in range(len(B)):
        str_b = str(B[i])
        flag = 0
        if len(str_b) > 1:
            for j in range(1,len(str_b)):
                #print(str_b[j-1], str_b[j])
                if str_b[j-1] <= str_b[j]:
                    flag = 1
                    pass
                elif str_b[j-1] > str_b[j]:
                    flag = 0
                    break
            if flag == 1:
                C.append(B[i])
        elif len(str_b) == 1:
            C.append(B[i])
    #print('c',C)
    if C == []:
        result = -1
    else:
        result = max(C)
    print('#{} {}' .format(test_case,result))


