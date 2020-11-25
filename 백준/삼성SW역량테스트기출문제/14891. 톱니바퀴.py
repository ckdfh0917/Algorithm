t1 = list(input())
t2 = list(input())
t3 = list(input())
t4 = list(input())

T = []
T.append(t1)
T.append(t2)
T.append(t3)
T.append(t4)

N = int(input())

def turn(t, d):
    if d == 1:
        temp = t[:-1]
        t = list(t[-1]) + temp
    else:
        t.append(t[0])
        t = t[1:]
    return t

for _ in range(N):
    n, d = map(int, input().split())

    if n == 1:
        if T[0][2] != T[1][6]:
            if T[1][2] != T[2][6]:
                if T[2][2] != T[3][6]:
                    T[3] = turn(T[3], -d)
                T[2] = turn(T[2], d)
            T[1] = turn(T[1], -d)
        T[n-1] = turn(T[n-1], d)
    elif n == 2:
        if T[1][6] != T[0][2]:
            T[0] = turn(T[0], -d)
        if T[1][2] != T[2][6]:
            if T[2][2] != T[3][6]:
                T[3] = turn(T[3], d)
            T[2] = turn(T[2], -d)
        T[n-1] = turn(T[n-1], d)

    elif n == 3:
        if T[2][6] != T[1][2]:
            if T[1][6] != T[0][2]:
                T[0] = turn(T[0], d)
            T[1] = turn(T[1], -d)
        if T[2][2] != T[3][6]:
            T[3] = turn(T[3], -d)
        T[n-1] = turn(T[n-1], d)

    elif n == 4:
        if T[3][6] != T[2][2]:
            if T[2][6] != T[1][2]:
                if T[1][6] != T[0][2]:
                    T[0] = turn(T[0], -d)
                T[1] = turn(T[1], d)
            T[2] = turn(T[2], -d)
        T[n-1] = turn(T[n-1], d)

    # print(T)
ans = int(T[0][0]) + int(T[1][0]) * 2 + int(T[2][0]) * 4 + int(T[3][0]) * 8
print(ans)