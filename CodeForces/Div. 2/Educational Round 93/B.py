t = int(input())

for _ in range(t):
    a = list(input())

    def max_one_len():
        res = 0
        c = 0
        for i in range(len(a)):
            if a[i] == '1':
                c += 1
                res = max(res, c)
            else:
                c = 0

        k = 0
        for i in range(len(a)):
            if a[i] == '1':
                k += 1
                if k == res:
                    for j in range(i-k+1, i+1):
                        a[j] = 0
                    break

            else:
                k = 0

        return res
    flag = 'A'
    ans = 0
    while '1' in a:
        if flag == 'A':
            ans += max_one_len()
            flag = 'B'
        else:
            max_one_len()
            flag = 'A'

    print(ans)