q = int(input())

def perm(temp, idx):
    global minV
    if temp >= B:
        minV = min(minV, temp-B)
    if 0 not in visited:
        return
    else:
        for i in range(idx, N):
            if visited[i] == 0:
                visited[i] = 1
                perm(temp+H[i], i)
                visited[i] = 0
        return

for test_case in range(1,q+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))


    visited = [0] * N
    minV = 1234567891
    p = []

    perm(0, 0)
    print('#{} {}'.format(test_case, minV))