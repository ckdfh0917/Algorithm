T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    k = y - x
    if k == 1:
        print(1)
    else:
        for n in range(k):
            tempA = n*n - n + 1
            tempB = (n+1)*(n+1) - (n+1) + 1
            if tempA <= k < tempB:
                mid = (tempB + tempA)//2
                if k < mid:
                    print(2*n-1)
                    break
                else:
                    print(2*n)
                    break

                    # ####
                    # asdadq12
                    # asdzcx
                    # zip(xz
                    #     xcz
                    # cz
                    # z
                    # c
                    # xzc
                    # zip())