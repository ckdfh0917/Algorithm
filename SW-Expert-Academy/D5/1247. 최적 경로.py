T = int(input())

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def find(v, cnt, idx, d):
    global minV
    # print(v, d)
    if cnt == N:
        a = v.index(N)
        d += distance(man[a][0], man[a][1], homeX, homeY)
        minV = min(minV, d)
        return
    elif d >= minV:
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = idx
                if d == 0:
                    tmp = distance(companyX, companyY, man[i][0], man[i][1])
                else:
                    a = v.index(idx-1)
                    tmp = distance(man[i][0], man[i][1], man[a][0], man[a][1])
                # print(tmp)
                find(v, cnt + 1, idx + 1, d+tmp)
                v[i] = 0
    return




for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    companyX = arr[0]
    companyY = arr[1]
    homeX = arr[2]
    homeY = arr[3]

    man = []
    for i in range(4, len(arr),2):
        X, Y = arr[i], arr[i+1]
        man.append([X, Y])
    # print(man)
    minV = 1234567891
    visited = [0] * N
    find(visited, 0, 1, 0)

    print('#{} {}'.format(test_case, minV))