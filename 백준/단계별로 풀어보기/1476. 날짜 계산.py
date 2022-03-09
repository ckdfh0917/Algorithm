E, S, M = map(int, input().split())

e = s = m = 0
for i in range(1, 10000):
    e += 1
    s += 1
    m += 1

    if e >= 16:
        e = 1
    if s >= 29:
        s = 1
    if m >= 20:
        m = 1

    if E == e and S == s and M == m:
        print(i)
        break

