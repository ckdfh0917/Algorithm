T = int(input())

def find(l, r, n, d):   # d: 오른쪽 +1, 왼쪽 -1
    global cnt
    m = (l+r) // 2
    # print('aa',l,r,m, d)
    # print('bb',n,cnt)
    # print()
    if A[m] == n:
        cnt += 1
        return
    elif l > r:
        return
    else:
        if A[m] < n:
            if d == 1:
                return
            else:
                find(m+1, r, n, +1)
        else:
            if d == -1:
                return
            else:
                find(l, m-1, n, -1)
    return



for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(M):
        n = B[i]
        find(0, N-1, n, 0)

    print('#{} {}' .format(test_case, cnt))