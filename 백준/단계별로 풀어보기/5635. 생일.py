n = int(input())

minIdx = -1
maxIdx = -1

names = []
# 가장 나이가 적은
d1 = 1
m1 = 1
y1 = 1990
# 가장 나이가 많은
d3 = 31
m3 = 12
y3 = 2010
for i in range(n):
    name, day, month, year = map(str, input().split())
    names.append(name)

    d2 = int(day)
    m2 = int(month)
    y2 = int(year)

    # print("name", name)
    # print("A", y1, m1, d1)
    # print("B", y2, m2, d2)
    # print("C", y3, m3, d3)
    if y1 < y2:
        y1 = y2
        m1 = m2
        d1 = d2
        minIdx = i
    elif y1 == y2:
        if m1 < m2:
            m1 = m2
            d1 = d2
            minIdx = i
        elif m1 == m2:
            if d1 < d2:
                d1 = d2
                minIdx = i

    if y3 > y2:
        y3 = y2
        m3 = m2
        d3 = d2
        maxIdx = i
    elif y3 == y2:
        if m3 > m2:
            m3 = m2
            d3 = d2
            maxIdx = i
        elif m3 == m2:
            if d3 > d2:
                d3 = d2
                maxIdx = i

print(names[minIdx])
print(names[maxIdx])
