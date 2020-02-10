
arr = [0, 4, 1, 3, 1, 2, 4, 1]



def CountSort(A, k, B):
    C = [0] * k
    print(C)

    # 배령의 원소 갯수 세기
    for i in range(len(A)):
        C[A[i]] += 1
    print('배령의 원소 갯수 세기')
    print(C)

    # 카운트 배열 조작하기 : 숫자들이 들어갈 자리를 표현하도록 내 앞 인덱스 숫자를  더해서 대입

    for i in range(len(C)-1):
        C[i+1] = C[i] + C[i+1]
    print('카운트 배열 조작하기 : 숫자들이 들어갈 자리를 표현하도록 내 앞 인덱스 숫자를  더해서 대입')
    print(C)

    # 정렬하기
    for i in range(len(A)-1,0,-1):
        C[A[i]] -=1
        B[C[A[i]]] = A[i]
    print('정렬하기')
    print(C)
    return B

print(CountSort(arr, 5, [0]*len(arr)))
