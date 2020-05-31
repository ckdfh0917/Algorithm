import sys
input = sys.stdin.readline
T = int(input())

def perm(v, cnt):
    global ans
    if cnt == x:
        tmp = 0
        for i in range(n):
            if v[i] == 1:
                tmp += a[i]
        if tmp % 2 == 1:
            ans = 'Yes'
        return
    elif ans == 'Yes':
        return
    else:
        for i in range(n):
            if v[i] == 0:
                v[i] = 1
                perm(v, cnt+1)
                v[i] = 0


for test_case in range(T):
    n, x = map(int, input().split())

    a = list(map(int, input().split()))
    # print(n, x)
    # print(a)

    ans = 'No'
    v = [0] * n
    perm(v, 0)
    print(ans)

    # cnt = 0
    # for i in range(n):
    #     if a[i] % 2 == 1:
    #         cnt += 1

