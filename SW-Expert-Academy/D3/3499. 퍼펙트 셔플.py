import sys
sys.stdin = open('input.txt', 'r')

q = int(input())

for test_case in range(1,q+1):
    num = int(input())
    munja = list(input().split())
    print('#{} '.format(test_case), end='')
    # print(munja)
    munja_len = len(munja)

    # 입력 받은 문자를 반 쪼개기
    A = munja[0:(munja_len-1)//2+1]
    B = munja[(munja_len-1)//2+1::]

    # 새로운 리스트에 A,B 하나 하나 채우기기
    result = []
    for i in range(munja_len//2+1):
        if i < len(A):
            result.append(A[i])
        if i < len(B):
            result.append(B[i])
    print(' '.join(result))
