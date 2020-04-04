q = int(input())

def cal(cnt, now):
    global ans
    if cnt == k:
        a = int(''.join(map(str, s)))
        ans = max(ans, a)
        return

    for i in range(now, len(s)):
        for j in range(i, len(s)):
            if i == j:
                continue
            if s[i] <= s[j]:
                s[i], s[j] = s[j], s[i]
                cal(cnt+1, i)
                s[i], s[j] = s[j], s[i]


for test_case in range(1,q+1):
    z = input().split()
    n = z[0]
    k = int(z[1])

    n = list(map(str, n))
    ans = 0
    s = n[:]
    cal(0, 0)
    print('#{} {}' .format(test_case, ans))