N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def find(x):
    s = 0
    e = N-1

    while s <= e:
        mid = (s+e) // 2

        if x == A[mid]:
            return True

        if x < A[mid]:
            e = mid - 1
        else:
            s = mid + 1

    return False

for i in range(M):
    if find(B[i]):
        print(1)
    else:
        print(0)
