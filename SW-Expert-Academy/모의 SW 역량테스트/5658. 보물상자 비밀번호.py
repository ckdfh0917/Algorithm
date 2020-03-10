q = int(input())

for test_case in range(1,q+1):
    N, K = map(int, input().split())
    num = list(input())
    temp = []
    for k in range(N):
        for i in range(0,N,N//4):
            n = num[i:i+N//4]
            b = N//4
            t = ''
            p = 0
            while p < b:
                t += n[p]
                p += 1
            t = '0x' + t
            r = int(t, 16)
            temp.append(r)

        a = num.pop()
        num.insert(0, a)
    temp = list(set(temp))
    temp.sort(reverse=True)
    print('#{} {}'.format(test_case, temp[K-1]))